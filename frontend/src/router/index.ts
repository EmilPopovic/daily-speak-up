import { createRouter, createWebHistory } from 'vue-router'

import Landing from '../views/Landing.vue'
import HomeView from '../views/HomeView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import OnboardingView from '../views/OnboardingView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/landing',
      name: 'landing',
      component: Landing
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: NotFoundView
    }
    ,
    {
      path: '/onboarding',
      name: 'onboarding',
      component: OnboardingView
    }
  ]
});

export default router;