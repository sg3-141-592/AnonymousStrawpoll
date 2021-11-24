<template>
    GeneratingToken: {{ token }}
</template>

<script>
import store from '../store'

export default {
    mounted() {
        store.commit('createInitialToken')
        this.token = store.state.token
    },
    data() {
        return {
            token: null
        }
    }
}

</script>
