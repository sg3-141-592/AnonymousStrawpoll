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
    path: '/view/:id',
    name: 'ViewPoll',
    component: ViewPoll
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
