<template>
  <div class="text-shadow-sm font-extrabold text-center">
    <h1>DailySpeakUp</h1>

    <!-- Gumb koji vodi na onboarding -->
    <Button 
      class="mt-[5rem] btnmy" 
      label="Onbarding" 
      @click="goToOnboarding"
    />
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

function goToOnboarding() {
  // Navigate to the onboarding route; adjust the route name/path if needed
  router.push({ name: 'Onboarding' }).catch(() => {});
}
</script>


