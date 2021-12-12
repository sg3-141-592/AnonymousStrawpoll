<template>
  <section class="hero is-small">
    <div class="hero-body">
      <p class="title">
        <span class="icon-text">
          <span class="icon">
            <i class="fas fa-bolt"></i>
          </span>
          <span>
            <router-link to="/" class="has-text-black">Live Strawpoll</router-link>
          </span>
        </span>
      </p>
    </div>
  </section>
  <section class="section pt-1 pb-1">
    <router-view/>
    <generate-user-id/>
  </section>
</template>

<script>
import GenerateUserId from './components/GenerateUserId.vue'

export default {
  components: {
    GenerateUserId
  },
}
</script>

<style>

</style>
