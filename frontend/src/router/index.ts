import { createRouter, createWebHistory } from 'vue-router'

import Landing from '../views/Landing.vue'
import HomeView from '../views/HomeView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import AuthCallbackView from '../views/AuthCallbackView.vue'
import PasswordlessCallbackView from '../views/PasswordlessCallbackView.vue'
import OnboardingView from '../views/OnboardingView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/auth/callback/google',
      name: 'auth-callback',
      component: AuthCallbackView
    },
    {
      path: '/auth/verify',
      name: 'passwordless-callback',
      component: PasswordlessCallbackView
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: NotFoundView
    },
    {
      path: '/onboarding',
      name: 'onboarding',
      component: OnboardingView
    }
  ]
});

export default router;