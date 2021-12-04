<template>
  <div class="home">
    <p>Get live anonymous feedback. Track sentiment. Make decisions based on data.</p>
    <br>
    <view-polls/>
    <create-poll/>
    <generate-user-id/>
  </div>
</template>

<script>
import CreatePoll from '../components/CreatePoll.vue'
import GenerateUserId from '../components/GenerateUserId.vue'
import ViewPolls from '../components/ViewPolls.vue'

export default {
  name: 'Home',
  components: {
    CreatePoll,
    GenerateUserId,
    ViewPolls
  }
}

</script>
