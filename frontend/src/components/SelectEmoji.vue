<template>
    <div class="container">
        <span class="icon is-large" v-for="font in fontList" :key="font">
            <a @click="emojiClicked(font)">
                <i :class="`fas ${font} fa-lg ${font==selectedEmoji ? 'fa-border has-text-black':''}`"></i>
            </a>
        </span>
    </div>
</template>

<script>
export default {
    methods: {
        emojiClicked(emojiName) {
            this.$emit('selectionChanged', emojiName)
        }
    },
    data() {
        return {
            fontList: ['fa-frown', 'fa-frown-open', 'fa-beer', 'fa-bell',
                'fa-grin-hearts', 'fa-laugh-beam', 'fa-atom', 'fa-sun',
                'fa-bug', 'fa-shield-alt', 'fa-flag-checkered', 'fa-traffic-light']
        }
    },
    props: ['selectedEmoji'],
    emits: ['selectionChanged']
}
</script>