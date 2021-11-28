<template>
    Select Emoji
    <div class="container">
        <span class="icon is-large" v-for="font in fontList" :key="font">
            <a @click="emojiClicked(font)">
                <i :class="`fas ${font} fa-lg ${font==selectedEmoji ? 'fa-border':''}`"></i>
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
                'fa-grin-hearts', 'fa-laugh-beam', 'fa-atom', 'fa-sun']
        }
    },
    props: ['selectedEmoji'],
    emits: ['selectionChanged']
}
</script>