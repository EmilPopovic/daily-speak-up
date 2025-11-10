<script setup lang="ts">
    import Login from './Login.vue';
    import Logout from './Logout.vue';
    import User from './User.vue';
    import NavBar from './NavBar.vue';
</script>

<template>
  <div class="flex flex-col w-full h-full bg-gray-300">
    <NavBar />
    
    <User />
    <div class="flex justify-between items-center p-4">
      <ul class="m-16">
        <li class="mb-2 hover:scale-105"><RouterLink to="/">Početna</RouterLink></li>
        <li class="mt-2 hover:scale-105"><RouterLink to="/about">O nama</RouterLink></li>
      </ul>
      <Login class="mr-8" />
      <Logout class="mr-8" />
    </div>

    <div class="bg-sky-400 w-[18rem] h-[18rem] rounded-[50%] flex justify-center items-center mx-auto my-20">
        <span class="pi pi-microphone"
              style="color:white; font-size: 14rem;"></span>
    </div>
    
  </div>
</template>

<style scoped>
</style>