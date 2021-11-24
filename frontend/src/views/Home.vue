<template>
  <div class="home">
    <create-poll/>
    <generate-user-id/>
  </div>
</template>

<script>
import CreatePoll from '../components/CreatePoll.vue'
import GenerateUserId from '../components/GenerateUserId.vue'

export default {
  name: 'Home',
  components: {
    CreatePoll,
    GenerateUserId
  }
}

</script>
