<template>
    <share-poll :url="this.$route.params.id"></share-poll>
    <br>
    <div v-if="pollData != null">
        <h1 class="title has-text-centered">{{ pollData.name }}</h1>
        <div>
            <span class="icon-text">
                <span class="icon">
                    <i :class="`fas ${ pollData.options.oneEmoji }`"></i>
                </span>
                <span>{{ pollData.options.one }}</span>
            </span>&nbsp;
            <input v-model="slider" type="range"
                min="0" max="1" step="0.01" @change="sliderChanged">&nbsp;
            <span class="icon-text">
                <span class="icon">
                    <i :class="`fas ${ pollData.options.twoEmoji }`"></i>
                </span>
                <span>{{ pollData.options.two }}</span>
            </span>
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
            console.log(this.slider)
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
            this.pollData = data
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