import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ViewPoll from '../views/ViewPoll.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/view-poll',
    name: 'View Poll',
    component: ViewPoll
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
