<template>
  <div class="home">
    <create-poll/>
    <generate-user-id/>
    <view-polls/>
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
