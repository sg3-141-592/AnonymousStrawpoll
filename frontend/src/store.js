import { createStore } from "vuex"
import { VuexPersistence } from 'vuex-persist'
import { v4 as uuidv4 } from 'uuid'

const store = createStore({
    state: {
        token: "TO_BE_DEFINED",
    },
    mutations: {
        createInitialToken(state) {
            if (state.token == "TO_BE_DEFINED") {
                state.token = uuidv4()
            }
        }
    },
    plugins: [new VuexPersistence().plugin]
})

export default store