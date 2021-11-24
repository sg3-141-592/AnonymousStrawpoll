<template>
  <div class="home">
    <create-poll/>
  </div>
</template>

<script>
import CreatePoll from '../components/CreatePoll.vue'

export default {
  name: 'Home',
  components: {
    CreatePoll
  }
}

</script>
