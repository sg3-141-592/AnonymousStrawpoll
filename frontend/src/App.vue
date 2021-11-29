<template>
  <section class="hero is-link is-small">
    <div class="hero-body">
      <p class="title">
        <span class="icon-text">
          <span class="icon">
            <i class="fas fa-info-circle"></i>
          </span>
          <span>
            <router-link to="/">Anon Strawpoll</router-link>
          </span>
        </span>
      </p>
    </div>
  </section>
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
