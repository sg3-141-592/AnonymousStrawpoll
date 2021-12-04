<template>
    <div class="field">
        <label class="label">Poll Name</label>
        <div class="control">
            <input v-model="pollName" class="input" type="text" placeholder="Poll Name">
        </div>
    </div>

    <div class="field">
        <label class="label">Option A</label>
        <div class="control">
            <input v-model="optionOne" class="input" type="text" placeholder="Let's do it">
        </div>
    </div>

    <div class="field">
        <select-emoji v-model:selectedEmoji="optionOneSelectedEmoji" @selectionChanged="data => optionOneSelectedEmoji = data"/>
    </div>

    <div class="field">
        <label class="label">Option B</label>
        <div class="control">
            <input v-model="optionTwo" class="input" type="text" placeholder="Let's hold off">
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
</template>

<script>
import store from '../store'
import router from '../router/index.js'
import SelectEmoji from '../components/SelectEmoji.vue'

export default {
    components: {
        SelectEmoji
    },
    methods: {
        createPoll: function () {
            let headers = new Headers({
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            });

            fetch(`/createPoll`, {
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
        }
    },
    data() {
        return {
            pollName: "",
            optionOne: "",
            optionOneSelectedEmoji: "fa-atom",
            optionTwo: "",
            optionTwoSelectedEmoji: "fa-frown-open",
        }
    }
}
</script>
