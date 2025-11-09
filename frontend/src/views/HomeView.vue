<script setup lang="ts">
  import Button from "primevue/button"
</script>

<template>
  <div class="text-shadow-sm font-extrabold">
    <h1>DailySpeakUp</h1>
  </div>

  <Button class="mt-[5rem] btnmy" 
          label="Onboarding" 
          onmousedown="alert('Ovaj gumbić još nikaj ne dela... 😞')"/>
</template>

<style scoped>
.btnmy {
  --p-button-border-radius: 9rem;
}
</style>
