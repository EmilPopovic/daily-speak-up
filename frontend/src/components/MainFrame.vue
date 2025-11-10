<script setup lang="ts">
    import Login from './Login.vue';
    import Logout from './Logout.vue';
    import User from './User.vue';
    import NavBar from './NavBar.vue';
    import RecordButton from './RecordButton.vue';
    import Fieldset from 'primevue/fieldset';
</script>

<template>
  <div class="flex flex-col items-center w-full h-full">
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

    <div class="border-black justify-center
                font-sans text-2xl font-semibold text-center my-20">
      <h1>Start practicing!</h1>
    </div>

    <RecordButton />

    <Fieldset legend="Tema za govor" :toggleable="true">
      <p class="m-0">
          Vaša će se tema za govor ovdje pojaviti nakon što pritisnete gumb za snimanje.
      </p>
    </Fieldset>
    
  </div>
</template>

<style scoped>

</style>