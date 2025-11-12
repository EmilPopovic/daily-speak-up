<script setup>
  import { RouterView, RouterLink } from 'vue-router';
  import { ref, onMounted, watch } from 'vue';
  import { useRoute } from 'vue-router';
  import LoginModal from './components/LoginModal.vue';
  import Logout from './components/Logout.vue';
  import User from './components/User.vue';
  import { isAuthenticated } from './auth';

  const route = useRoute();
  const authenticated = ref(false);

  const checkAuth = async () => {
    authenticated.value = await isAuthenticated();
  };

  onMounted(async () => {
    await checkAuth();
  });

  // Re-check authentication when route changes (e.g., after OAuth callback)
  watch(() => route.path, async () => {
    await checkAuth();
  });
</script>

<template>
  <RouterView />
</template>