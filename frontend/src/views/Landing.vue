<script setup lang="ts">
  import Button  from "primevue/button";
  import Avatar from 'primevue/avatar'
  import { useRouter, useRoute } from 'vue-router';
  import { ref, computed } from 'vue';
  import Login from '../components/Login.vue';

  const router = useRouter();
  const goToOnboarding = () => router.push('/onboarding')

  // provjera da li smo na početnoj
  const isHome = computed(() => useRoute().path === '/')

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
  <div class="flex flex-col justify-evenly items-center w-full h-[70vh]">

    <div class=" mb-[5vh] ">
      <img src="../assets/DSU_logo.svg" alt="DailySpeakUp Logo" class="w-48 h-48" />
    </div>

    <div>
      <h1>DailySpeakUp</h1>
    </div>

    <div class="flex flex-col justify-center items-center">
      <Login />

      <Button 
        class="mt-[2vh]" 
        label="Onbarding" 
        @click="goToOnboarding"
      />
    </div>
  </div>

  <footer
      v-if="isHome"
      class="mt-auto bg-gray-50 py-8 border-t w-full h-[30vh]"
  >
    <div class="flex flex-row flex-wrap justify-center">
      <div
        v-for="member in teamSet"
        :key="member.name"
        class="mx-[2vw] my-3 text-center"
      >
        <Avatar :image="member.url" class="medium lg:xlarge mr-2" shape="circle" />
        <div class="mt-2 font-medium">{{ member.name }}</div>
      </div>
    </div>
  </footer>

</template>



