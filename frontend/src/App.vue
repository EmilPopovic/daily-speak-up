<script setup>
  import { RouterView, RouterLink } from 'vue-router';
  import { ref, onMounted } from 'vue';
  import Login from './components/Login.vue';
  import Signup from './components/Signup.vue';
  import Logout from './components/Logout.vue';
  import User from './components/User.vue';
  import { isAuthenticated } from './auth';

  const authenticated = ref(false);

  onMounted(async () => {
    authenticated.value = await isAuthenticated();
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
          <Login />
          <Signup />
        </template>
        <template v-else>
          <User />
          <Logout />
        </template>
      </div>
    </div>
    <RouterView />
</template>