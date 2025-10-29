<script setup>
  import { RouterView, RouterLink } from 'vue-router';
  import Login from './components/Login.vue';
  import Logout from './components/Logout.vue';
  import User from './components/User.vue';
</script>

<template>
    <User />
    <div class="flex justify-between items-center p-4">
      <ul class="m-16">
        <li class="mb-2 hover:scale-105"><RouterLink to="/">Početna</RouterLink></li>
        <li class="mt-2 hover:scale-105"><RouterLink to="/about">O nama</RouterLink></li>
      </ul>
      <Login class="mr-8" />
      <Logout class="mr-8" />
    </div>
    <RouterView />
</template>