<template>
    Select Emoji TextBox
    <div class="field">
        <p class="control has-icons-right">
            <input @focus="inputFocus = true" @blur="setTimeout(() => inputFocus = false, 100)"
                class="input">
            <span class="icon is-small is-right">
                <i :class="`fas ${selectedEmoji}`"></i>
            </span>
        </p>
    </div>
    <div class="field">
        <div v-if="inputFocus">
            <select-emoji v-model:selectedEmoji="selectedEmoji"  @selectionChanged="data => selectedEmoji = data"/>
        </div>
    </div>
</template>

<script>
import SelectEmoji from '../components/SelectEmoji.vue'
export default {
    components: {
        SelectEmoji
    },
    // watch: {
    //     selectedEmoji: function() {
    //         this.inputFocus = false
    //     }
    // },
    data() {
        return {
            selectedEmoji: "fa-atom",
            inputFocus: false
        }
    }
}
</script>