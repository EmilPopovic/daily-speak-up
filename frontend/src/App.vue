<script setup>
  import { RouterView, RouterLink } from 'vue-router';
  import { ref, onMounted, watch } from 'vue';
  import { useRoute } from 'vue-router';
  import GoogleLogin from './components/GoogleLogin.vue';
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
    <div class="flex justify-between items-center p-4">
      <ul class="m-16">
        <li class="mb-2 hover:scale-105"><RouterLink to="/">Početna</RouterLink></li>
        <li class="mt-2 hover:scale-105"><RouterLink to="/about">O nama</RouterLink></li>
      </ul>
      <div class="flex items-center gap-4 mr-8">
        <template v-if="!authenticated">
          <GoogleLogin />
        </template>
        <template v-else>
          <User />
          <Logout />
        </template>
      </div>
    </div>
    <RouterView />
</template>