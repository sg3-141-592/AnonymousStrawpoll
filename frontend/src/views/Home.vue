<template>
  <div class="home">
    Anonymously get feedback on how people are feeling. Track how peoples opinions change over time.
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
