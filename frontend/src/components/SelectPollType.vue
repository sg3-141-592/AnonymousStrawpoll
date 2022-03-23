<template>
    <div class="field">
        <div class="control">
            <label v-for="(pollType, index) in POLL_TYPES" :key="pollType" class="radio">
                <input type="radio" name="foobar" :value="pollType" :id="pollType"
                    @change="$emit('changed', pollType)" :checked="index === 0">
                {{ pollType }}
                <i v-if="pollType == 'Traditional'" class="fas fa-poll"></i>
                <i v-if="pollType == 'Slider'" class="fas fa-sliders-h"></i> 
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