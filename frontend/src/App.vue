<script setup>
  import { RouterView, RouterLink } from 'vue-router';
</script>

<template>
    <ul class="m-[4rem]">
      <li class="mb-2 hover:scale-105"><RouterLink to="/">Početna</RouterLink></li>
      <li class="mt-2 hover:scale-105"><RouterLink to="/about">O nama</RouterLink></li>
      <li class="mt-2 hover:scale-105"><RouterLink to="/login">Login</RouterLink></li>
    </ul>
    <RouterView />
</template>