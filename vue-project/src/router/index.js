import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/NavigationBar.vue'
import ViewView from '../views/ViewView.vue'
import AddView from '../views/AddView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }
    ,
    {
      path: '/ViewView',
      name: 'ViewView',
      component: ViewView
    },
    {
      path: '/AddView',
      name: 'AddView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AddView
    }
  ]
})

export default router
