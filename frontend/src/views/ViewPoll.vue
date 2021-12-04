<template>
    <share-poll :url="this.$route.params.id"></share-poll>
    <div v-if="pollData != null">
        <h1 class="title has-text-centered">{{ pollData.name }}</h1>
        <!-- Alternative Layout -->
        <div>
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
        <average-graph :chartData="analyticsData" :axisLabels="{one:pollData.options.one, two:pollData.options.two}"/>
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
        updateVotingDetails: function(data) {
            this.votingData = data
        },
        updateAnalyticsDetails: function(data) {
            this.analyticsData = data
        }
    },
    data() {
        return {
            pollData: null,
            votingData: null,
            analyticsData: null,
            slider: 0.50
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