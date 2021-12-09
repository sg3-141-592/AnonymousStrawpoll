<template>
    <share-poll :url="this.$route.params.id"></share-poll>
    <div v-if="pollData != null">
        <h1 class="title has-text-centered mb-2">{{ pollData.name }}</h1>
        <p><i class="fas fa-user"></i> {{ userCount }} users</p>
        <!-- Alternative Layout -->
        <div class="pt-3">
            <table width=100%>
                <tr>
                    <td width=50%>
                        <span class="icon-text">
                            <span class="icon">
                                <i :class="`fas ${ pollData.options.oneEmoji }`"></i>
                            </span>
                            <span>{{ pollData.options.one }}</span>
                        </span>
                    </td>
                    <td width=50% class="has-text-right">
                        <span class="icon-text">
                            <span class="icon">
                                <i :class="`fas ${ pollData.options.twoEmoji }`"></i>
                            </span>
                            <span>{{ pollData.options.two }}</span>
                        </span>
                    </td>
                </tr>
            </table>
            <table width=100%>
                <tr>
                    <td class="has-text-centered" width=100%>
                        <input style="width: 100%;" v-model="slider" type="range"
                            min="0" max="1" step="0.01" @change="sliderChanged">
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <br>
    <div v-if="analyticsData != null">
        <average-graph :chartData="analyticsData" :latestPoints="latestPoints" :axisLabels="{one:pollData.options.one, two:pollData.options.two}"/>
    </div>
    <div class="notification is-info is-light">
        <p class="mb-2">Try creating your own poll</p>
        <div class="field">
            <div class="control">
                <button  @click="$router.push({name: 'Home'})" class="button is-info">
                    <span class="icon">
                        <i class="fas fa-plus"></i>
                    </span>
                    <span>Create</span>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import store from '../store'
import AverageGraph from '../components/AverageGraph.vue'
import SharePoll from  '../components/SharePoll.vue'

export default {
    components: {
        AverageGraph,
        SharePoll
    },
    mounted() {
        this.$socket.emit('join', {
            pollId: this.$route.params.id,
            userId: store.state.token
        })
    },
    methods: {
        sliderChanged: function () {
            this.$socket.emit('vote', {
                value: this.slider,
                pollId: this.$route.params.id,
                userId: store.state.token
            })
        }
    },
    sockets: {
        connect: function() {
            console.log("SocketIO connected")
        },
        updatePollDetails: function(data) {
            this.pollData = data,
            this.slider = data.latestVote
        },
        updateAnalyticsDetails: function(data) {
            this.analyticsData = data.averageData,
            this.userCount = data.userCount,
            this.latestPoints = data.latestPoints
        }
    },
    data() {
        return {
            pollData: null,
            analyticsData: null,
            latestPoints: null,
            slider: 0.50,
            userCount: 0,
        }
    }
}
</script>

<style scoped>
    input[type="range"] {
        width: 70%;
        text-align: center;
        vertical-align: bottom;
    }
</style>