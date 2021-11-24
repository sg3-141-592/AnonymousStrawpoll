import { createStore } from "vuex"
import { VuexPersistence } from 'vuex-persist'

const store = createStore({
    state: {
        token: "TO_BE_DEFINED",
    },
    mutations: {
        createInitialToken(state) {
            if (state.token == "TO_BE_DEFINED") {
                state.token = "SeanToken1abc"
            }
        }
    },
    plugins: [new VuexPersistence().plugin]
})

export default store