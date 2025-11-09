<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Button from 'primevue/button'
import Avatar from 'primevue/avatar'

// router za preusmjeravanje
const router = useRouter()

function goToOnboarding() {
  router.push('/onboarding')
}

// podaci o timu
const teamSet = ref([
  { url: 'https://avatars.githubusercontent.com/u/44684310?v=4', name: 'Kristijan Bilanović' },
  { url: 'https://avatars.githubusercontent.com/u/205453688?v=4', name: 'Lara Brečić' },
  { url: 'https://avatars.githubusercontent.com/u/236687211?v=4', name: 'Lara Desnica' },
  { url: 'https://avatars.githubusercontent.com/u/219036118?v=4', name: 'Mate Jakovljev' },
  { url: 'https://avatars.githubusercontent.com/u/74995193?v=4', name: 'Matej Jurasić' },
  { url: 'https://avatars.githubusercontent.com/u/104315710?v=4', name: 'Emil Popović' },
  { url: 'https://avatars.githubusercontent.com/u/153128323?v=4', name: 'Nika Valić' },
  
])
</script>

<template>
  <!-- Sekcija s avatarima -->
  <div class="flex flex-row flex-wrap justify-center mt-10">
    <div 
      v-for="(member, i) in teamSet" 
      :key="i" 
      class="ml-5 mr-5 text-center"
    >
      <Avatar :image="member.url" class="mr-2" size="xlarge" shape="circle" />
      <div class="mt-2 font-medium">{{ member.name }}</div>
    </div>
  </div>
</template>

<style scoped>
.btnmy {
  --p-button-border-radius: 9rem;
}
</style>