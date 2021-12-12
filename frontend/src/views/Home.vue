<template>
  <div class="home">
    <p>Get live anonymous feedback. Track sentiment. Make decisions based on data.</p>
    <br>
    <view-polls/>
    <create-poll/>
  </div>
</template>

<script>
import CreatePoll from '../components/CreatePoll.vue'
import ViewPolls from '../components/ViewPolls.vue'

export default {
  name: 'Home',
  components: {
    CreatePoll,
    ViewPolls
  }
}

</script>
