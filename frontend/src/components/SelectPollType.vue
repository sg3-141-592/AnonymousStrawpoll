<template>
    <div class="field">
        <div class="control">
            <label v-for="pollType in POLL_TYPES" :key="pollType" class="radio">
                <input type="radio" name="foobar">
                {{ pollType }}
            </label>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            POLL_TYPES: ["Slider", "Traditional"]
        }
    }
}
</script>