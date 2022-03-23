<template>
    <div v-if="pollList != null && pollList.length > 0">
        <h2 class="subtitle is-4">Your Recent Polls</h2>
    </div>
    <div v-if="pollList != null && pollList.length > 0" class="content">
        <ul>
            <li v-for="poll in pollList" :key="poll.url">
                <router-link :to="{ name: 'ViewPoll', params: { 'id': poll.url } }">{{ poll.name }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import store from '../store'

export default {
    mounted() {
        fetch(`/api/getPolls?userId=${store.state.token}`, {
            method: 'GET'
        })
            .then(response => response.json())
            .then(data => this.pollList = data)
    },
    data() {
        return {
            pollList: null
        }
    }
}
</script>
