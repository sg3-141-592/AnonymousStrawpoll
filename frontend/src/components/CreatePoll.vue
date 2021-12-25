<template>
    <select-poll-type/>
    <div class="field">
        <label class="label">Poll Name</label>
        <div class="control">
            <input v-model="pollName" class="input" type="text" placeholder="Poll Name">
        </div>
    </div>

    <div class="field">
        <label class="label">Option A</label>
        <div class="control">
            <input v-model="optionOne" class="input" type="text" placeholder="Let's do it" maxlength="60">
        </div>
    </div>

    <div class="field">
        <select-emoji v-model:selectedEmoji="optionOneSelectedEmoji" @selectionChanged="data => optionOneSelectedEmoji = data"/>
    </div>

    <div class="field">
        <label class="label">Option B</label>
        <div class="control">
            <input v-model="optionTwo" class="input" type="text" placeholder="Let's hold off" maxlength="60">
        </div>
    </div>

    <div class="field">
        <select-emoji v-model:selectedEmoji="optionTwoSelectedEmoji"  @selectionChanged="data => optionTwoSelectedEmoji = data"/>
    </div>

    <div class="field">
        <div class="control">
            <button class="button is-link" @click="createPoll()">Create</button>
        </div>
    </div>

    <div class="pt-4" v-if="errorMessage.length > 0">
        <div class="notification is-warning is-light">
            <p v-for="error in errorMessage" :key="error">{{ error }}</p>
        </div>
    </div>
</template>

<script>
import store from '../store'
import router from '../router/index.js'
import SelectEmoji from '../components/SelectEmoji.vue'
import SelectPollType from '../components/SelectPollType.vue'

export default {
    components: {
        SelectEmoji,
        SelectPollType
    },
    methods: {
        createPoll: function () {
            // Check if the different options have been populated
            let newErrorMessage = []
            if (this.pollName.length == 0) {
                newErrorMessage.push("Poll must have a name")
            }
            if (this.optionOne.length == 0) {
                newErrorMessage.push("Poll must have an Option A")
            }
            if (this.optionTwo.length == 0) {
                newErrorMessage.push("Poll must have an Option B")
            }
            if (newErrorMessage.length > 0) {
                this.errorMessage = newErrorMessage
                return false;
            }

            let headers = new Headers({
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            });

            fetch(`/api/createPoll`, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    pollName: this.pollName,
                    optionOne: this.optionOne,
                    optionOneEmoji: this.optionOneSelectedEmoji,
                    optionTwo: this.optionTwo,
                    optionTwoEmoji: this.optionTwoSelectedEmoji,
                    userId: store.state.token
                })
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
            pollName: "",
            optionOne: "",
            optionOneSelectedEmoji: "fa-atom",
            optionTwo: "",
            optionTwoSelectedEmoji: "fa-frown-open",
            errorMessage: []
        }
    }
}
</script>
