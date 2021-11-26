<template>
    <div v-if="pollData != null">
        <h1 class="title">{{ pollData.name }}</h1>
        <div class="columns is-fullwidth">
            <div class="column is-one-quarter">
                {{ pollData.options.one }}
            </div>
            <div class="column is-half">
                <input v-model="slider" type="range"
                    min="0" max="1" step="0.01" @change="sliderChanged">
            </div>
            <div class="column is-one-quarter">
                {{ pollData.options.two }}
            </div>
        </div>
    </div>
</template>

<script>
import store from '../store'

export default {
    mounted() {
        this.$socket.emit('join', {
            'pollId': this.$route.params.id,
            'userId': store.state.token
        })
    },
    methods: {
        sliderChanged: function () {
            console.log(this.slider)
        }
    },
    sockets: {
        connect: function() {
            console.log("SocketIO connected")
        },
        update: function(data) {
            this.pollData = data
        }
    },
    data() {
        return {
            pollData: null,
            slider: 0.50
        }
    }
}
</script>

<style scoped>
    input[type="range"] {
        width: 400px;
    }
</style>