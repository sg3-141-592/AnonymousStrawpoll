<template>
    <div class="notification is-info is-light">
        <p>Invite others to join your poll</p>
        <br>
        <div class="field has-addons">
            <div class="control is-expanded">
                <input class="input is-info" :value="fullUrl" type="text" readonly ref="shareLink">
            </div>
            <div class="control">
                <button @click="copyURL()" class="button is-info">
                    <span class="icon">
                        <i class="fas fa-link"></i>
                    </span>
                    <span>Copy Link</span>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['url'],
    computed: {
        fullUrl: function () {
            return window.location.href// + this.url
        }
    },
    methods: {
        copyURL() {
            var Url = this.$refs.shareLink;
            Url.innerHTML = window.location.href;
            console.log(Url.innerHTML)
            Url.select();
            document.execCommand("copy");
        }
    }
}
</script>
