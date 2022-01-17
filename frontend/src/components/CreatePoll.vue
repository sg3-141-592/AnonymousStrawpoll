<template>
    <select-poll-type @changed="data => pollType = data"/>
    
    <div v-if="pollType == 'Slider'">
        <create-sentiment-poll @pollData="data => pollData = data" @errorMessages="data => errorMessages = data"/>
    </div>
    <div v-else-if="pollType == 'Traditional'">
        <create-traditional-poll/>
    </div>

    <div class="field">
        <div class="control">
            <button class="button is-link" @click="createPoll()">Create</button>
        </div>
    </div>

    <div class="pt-4" v-if="errorMessages.length > 0">
        <div class="notification is-warning is-light">
            <p v-for="error in errorMessages" :key="error">{{ error }}</p>
        </div>
    </div>
</template>

<script>
import store from '../store'
import router from '../router/index.js'
import SelectPollType from '../components/SelectPollType.vue'
import CreateSentimentPoll from '../components/CreateSentimentPoll.vue'
import CreateTraditionalPoll from '../components/CreateTraditionalPoll.vue'

export default {
    components: {
        SelectPollType,
        CreateSentimentPoll,
        CreateTraditionalPoll
    },
    methods: {
        createPoll: function () {

            let headers = new Headers({
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            });

            // Add the userId to the poll data
            let pollDataUserId = this.pollData
            pollDataUserId.userId = store.state.token

            fetch(`/api/createPoll`, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(pollDataUserId)
            })
                .then(response => response.json())
                .then(data => router.push(
                    {name: 'ViewPoll', params: {id: data.id}}
                ));
            
            return true
        }
    },
    data() {
        return {
            pollData: null,
            pollType: "Slider",
            errorMessages: []
        }
    }
}
</script>
