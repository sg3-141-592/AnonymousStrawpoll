<template>
    <div class="card">

        <header class="card-header">
            <p class="card-header-title">
                Create Poll
            </p>
        </header>

        <div class="card-content">
            <div class="content">

                <div class="field">
                    <label class="label">Poll Name</label>
                    <div class="control">
                        <input v-model="pollName" class="input" type="text" placeholder="Poll Name">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Option 1</label>
                    <div class="control">
                        <input v-model="optionOne" class="input" type="text" placeholder="Option 1">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Option 2</label>
                    <div class="control">
                        <input v-model="optionTwo" class="input" type="text" placeholder="Option 2">
                    </div>
                </div>

            </div>
        </div>

        <footer class="card-footer">
            <a class="card-footer-item" @click="createPoll()">Create</a>
        </footer>

    </div>
</template>

<script>
import store from '../store'

export default {
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
                    optionTwo: this.optionTwo,
                    userId: store.state.token
                })
            })
                .then(response => response.json())
                .then(data => console.log(data));
        }
    },
    data() {
        return {
            pollName: "",
            optionOne: "",
            optionTwo: "",
        }
    }
}
</script>
