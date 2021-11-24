<template>
  <div id="nav">
    <router-link to="/">Home</router-link> | 
    <router-link to="/view-poll">View Poll</router-link>
  </div>
  <section class="section">
    <router-view/>
  </section>
</template>

<script>
export default {
  setup() {
    
  },
}
</script>

<style>

</style>
