import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-3-socket.io'

import './../node_modules/bulma/css/bulma.css'
import './../node_modules/@fortawesome/fontawesome-free/css/all.min.css'

const app = createApp(App)
app.use(router)
app.use(store)
app.use(new VueSocketIO({
    debug: false,
    connection: '/api/',
    vuex: {
        store,
        actionPrefix: 'SOCKET_',
        mutationPrefix: 'SOCKET_'
    },
}))
app.mount('#app')
