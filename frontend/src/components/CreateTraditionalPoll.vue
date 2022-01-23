<template>
    <div class="field">
        <label class="label">Poll Name</label>
        <div class="control">
            <input v-model="pollName" class="input" type="text"
                placeholder="Poll Name">
        </div>
    </div>
    <div class="field">
        <select-emoji-text-box/>
    </div>
</template>

<script>
import SelectEmojiTextBox from '../components/SelectEmojiTextBox.vue'

export default {
    components: {
        SelectEmojiTextBox
    },
    data() {
        return {
            pollName: ""
        }
    }
}
</script>
