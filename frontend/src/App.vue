<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter, useRoute, RouterView, RouterLink } from 'vue-router'

import Login from './components/Login.vue'
import User from './components/User.vue'

import Avatar from 'primevue/avatar'

const router = useRouter()
const route = useRoute()

const goToOnboarding = () => router.push('/onboarding')

// provjera da li smo na početnoj
const isHome = computed(() => route.path === '/')

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
  <div class="min-h-screen flex flex-col">
    <!-- Header -->
    <header class="flex justify-between items-center p-4">
      <nav>
        <ul class="flex gap-6 m-0 p-0">
          <li class="hover:scale-105 transition"><RouterLink to="/">Početna</RouterLink></li>
          <li class="hover:scale-105 transition"><RouterLink to="/about">O nama</RouterLink></li>
          <li class="hover:scale-105 transition"><RouterLink to="/contact">Kontakt</RouterLink></li>
        </ul>
      </nav>
      <div class="flex items-center gap-4">
        <Login />
        <Logout />
      </div>
    </header>

    <!-- Glavni sadržaj -->
    <main class="flex-1">
      <User />

      <div class="flex justify-center mt-10">
        <button
          type="button"
          class="btnmy px-6 py-3 border rounded-full hover:scale-105 transition"
          @click="goToOnboarding"
        >
          Onboarding
        </button>
      </div>

      <section class="mt-10">
        <RouterView />
      </section>
    </main>

    <!-- Footer s avatarima (samo na početnoj) -->
    <footer
      v-if="isHome"
      class="mt-auto bg-gray-50 py-8 border-t transition-all duration-300"
    >
      <div class="flex flex-row flex-wrap justify-center">
        <div
          v-for="member in teamSet"
          :key="member.name"
          class="mx-5 my-3 text-center"
        >
          <Avatar :image="member.url" size="xlarge" shape="circle" class="mr-2" />
          <div class="mt-2 font-medium">{{ member.name }}</div>
        </div>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.btnmy {
  --p-button-border-radius: 9rem;
}
</style>
