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
