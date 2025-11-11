<script setup lang="ts">
    import NavBar from './NavBar.vue';
    import RecordButton from './RecordButton.vue';
    import Fieldset from 'primevue/fieldset';
</script>

<template>
  <div class="bg-sky-100 flex flex-col items-center w-[65%] h-full">
    <NavBar />

    <div class="border-black justify-center
                font-sans text-2xl font-semibold text-center my-[5%]">
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