import { createRouter, createWebHistory } from 'vue-router'
import ProfilePage from '../pages/ProfilePage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue'),
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue'),
  },
  {
    path: '/events',
    name: 'events',
    component: () => import('../pages/EventsPage.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../pages/LoginPage.vue'),
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../pages/SignupPage.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../pages/RegistrationPage.vue'),
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
