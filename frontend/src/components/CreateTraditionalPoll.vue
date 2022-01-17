<template>
    <div class="field">
        <label class="label">Poll Name</label>
        <div class="control">
            <input v-model="pollName" class="input" type="text"
                placeholder="Poll Name">
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            pollName: ""
        }
    }
}
</script>
