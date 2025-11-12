import { createRouter, createWebHistory } from 'vue-router'

import Landing from '../views/Landing.vue'
import HomeView from '../views/HomeView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import AuthCallbackView from '../views/AuthCallbackView.vue'
import PasswordlessCallbackView from '../views/PasswordlessCallbackView.vue'
import OnboardingView from '../views/OnboardingView.vue'
import { isAuthenticated } from '../auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing,
      meta: { requiresGuest: true }
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta: { requiresAuth: true }
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
      component: OnboardingView,
      meta: { requiresAuth: true }
    }
  ]
});

// Navigation guard to handle authentication routing
router.beforeEach(async (to, _from, next) => {
  const authenticated = await isAuthenticated();

  // If user is authenticated and trying to access landing page
  if (authenticated && to.meta.requiresGuest) {
    try {
      // Check user's onboarding status
      const apiDomain = import.meta.env.VITE_API_DOMAIN || 'http://localhost:8123';
      const response = await fetch(`${apiDomain}/api/v1/user/me`, {
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        }
      });

      if (response.ok) {
        const userData = await response.json();
        
        // If onboarding is not complete, redirect to onboarding
        if (userData.onboarding_status === 'PENDING' || userData.onboarding_status === 'IN_PROGRESS') {
          return next('/onboarding');
        } else {
          // Onboarding complete, redirect to home
          return next('/home');
        }
      } else {
        // If we can't fetch user data, default to onboarding
        return next('/onboarding');
      }
    } catch (error) {
      console.error('Error checking user status:', error);
      // On error, default to onboarding
      return next('/onboarding');
    }
  }

  // If route requires auth and user is not authenticated
  if (to.meta.requiresAuth && !authenticated) {
    return next('/');
  }

  // Otherwise, proceed as normal
  next();
});

export default router;