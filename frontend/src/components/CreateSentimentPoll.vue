<template>
    <div class="field">
        <label class="label">Poll Name</label>
        <div class="control">
            <input v-model="pollName" class="input" type="text" placeholder="Poll Name">
        </div>
    </div>

    <div class="field">
        <label class="label">Option A</label>
        <div class="control">
            <input v-model="optionOne" class="input" type="text" placeholder="Let's do it" maxlength="60">
        </div>
    </div>

    <div class="field">
        <select-emoji v-model:selectedEmoji="optionOneSelectedEmoji" @selectionChanged="data => optionOneSelectedEmoji = data"/>
    </div>

    <div class="field">
        <label class="label">Option B</label>
        <div class="control">
            <input v-model="optionTwo" class="input" type="text" placeholder="Let's hold off" maxlength="60">
        </div>
    </div>

    <div class="field">
        <select-emoji v-model:selectedEmoji="optionTwoSelectedEmoji"  @selectionChanged="data => optionTwoSelectedEmoji = data"/>
    </div>

</template>

<script>
import SelectEmoji from '../components/SelectEmoji.vue'

export default {
    components: {
        SelectEmoji
    },
    methods: {
        checkErrors: function() {
             // Check if the different options have been populated
            let newErrorMessage = []
            if (this.pollName.length == 0) {
                newErrorMessage.push("Poll must have a name")
            }
            if (this.optionOne.length == 0) {
                newErrorMessage.push("Poll must have an Option A")
            }
            if (this.optionTwo.length == 0) {
                newErrorMessage.push("Poll must have an Option B")
            }
            return newErrorMessage
        }
    },
    watch: {
        $data: {
            handler: function() {
                this.$emit('pollData', this.$data)
                this.$emit('errorMessages', this.checkErrors())
            },
            deep: true
        }
    },
    emits: ["pollData", "errorMessages"],
    data() {
        return {
            pollName: "",
            optionOne: "",
            optionOneSelectedEmoji: "fa-atom",
            optionTwo: "",
            optionTwoSelectedEmoji: "fa-frown-open"
        }
    }
}
</script>