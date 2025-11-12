<script setup lang="ts">
import Button from 'primevue/button'
import Avatar from 'primevue/avatar'
import { useRouter, useRoute } from 'vue-router'
import { ref, computed } from 'vue'
import Login from '../components/Login.vue'

const router = useRouter()
const goToOnboarding = () => router.push('/onboarding')
const isHome = computed(() => useRoute().path === '/')

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
  <div class="min-h-screen flex flex-col bg-gradient-to-b from-white to-slate-50/60">
    <!-- HEADER s navigacijom iznad loga -->
    <header class="relative">
      <div class="max-w-6xl mx-auto px-6 pt-28 pb-20 sm:pt-32 sm:pb-24 flex flex-col items-center">
       <nav class="absolute inset-x-0 top-0 flex justify-end px-6 sm:px-10 py-4 z-10">
        <Login/>
       </nav>


        <!-- Logo -->
        <img
          src="../assets/DSU_logo.svg"
          alt="DailySpeakUp Logo"
          class="w-28 h-28 sm:w-40 sm:h-40 mb-8"
        />

        <!-- Naslov + opis (centrirano) -->
        <div class="text-center max-w-2xl">
          <h1 class="text-3xl sm:text-4xl font-semibold tracking-tight text-slate-800">
            DailySpeakUp
          </h1>
          <p class="mt-8 text-base sm:text-lg text-slate-700 leading-relaxed">
            Aplikacija za kratke, svakodnevne vježbe javnog govora s povratnom informacijom.
          </p>
          <p class="mt-3 text-base text-slate-700 leading-relaxed">
            Vježba traje 1–2 minute. Snimiš govor, a mi ti vratimo nekoliko jasnih napomena:
            što ti ide dobro i što možeš probati idući put. Nije natjecanje, nego mali dnevni korak.
          </p>
          <p class="mt-3 text-sm text-slate-600 leading-relaxed">
            Dobro došli su svi — učenici, studenti, predavači, timovi… i svi koji jednostavno žele
            zvučati sigurnije.
          </p>
        </div>
      </div>
    </header>

    <!-- KAKO RADI -->
    <section class="max-w-6xl mx-auto px-6 py-14 sm:py-16">
      <h2 class="text-2xl sm:text-3xl font-semibold text-center">Kako to izgleda u praksi</h2>
      <p class="text-slate-600 text-center mt-2">Tri jednostavna koraka</p>

      <div class="mt-10 grid grid-cols-1 sm:grid-cols-3 gap-6">
        <div class="rounded-xl border bg-white p-6 text-center">
          <div class="text-4xl">🎯</div>
          <h3 class="mt-3 font-semibold text-lg">Odabir teme</h3>
          <p class="mt-2 text-slate-700 leading-relaxed">Uzmi našu dnevnu temu ili upiši svoju.</p>
        </div>
        <div class="rounded-xl border bg-white p-6 text-center">
          <div class="text-4xl">🎤</div>
          <h3 class="mt-3 font-semibold text-lg">Kratko snimanje</h3>
          <p class="mt-2 text-slate-700 leading-relaxed">1–2 minute govora na webu ili mobitelu.</p>
        </div>
        <div class="rounded-xl border bg-white p-6 text-center">
          <div class="text-4xl">💬</div>
          <h3 class="mt-3 font-semibold text-lg">Povratna informacija</h3>
          <p class="mt-2 text-slate-700 leading-relaxed">Sažeti savjeti za sljedeći pokušaj.</p>
        </div>
      </div>
    </section>

    <!-- BENEFITI -->
    <section class="max-w-6xl mx-auto px-6 py-14 sm:py-16">
      <h2 class="text-2xl sm:text-3xl font-semibold text-center">Što dobiješ</h2>
      <div class="mt-10 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="rounded-xl border bg-white p-6">
          <div class="text-2xl">🗣️</div>
          <h3 class="mt-3 font-semibold">Redovitu praksu</h3>
          <p class="mt-2 text-slate-700 leading-relaxed">Kratke vježbe koje stanu u dan.</p>
        </div>
        <div class="rounded-xl border bg-white p-6">
          <div class="text-2xl">⏰</div>
          <h3 class="mt-3 font-semibold">Mali koraci</h3>
          <p class="mt-2 text-slate-700 leading-relaxed">Dovoljno je pet minuta.</p>
        </div>
        <div class="rounded-xl border bg-white p-6">
          <div class="text-2xl">🤖</div>
          <h3 class="mt-3 font-semibold">Jasan feedback</h3>
          <p class="mt-2 text-slate-700 leading-relaxed">Bez praznih fraza — konkretne smjernice.</p>
        </div>
        <div class="rounded-xl border bg-white p-6">
          <div class="text-2xl">🔒</div>
          <h3 class="mt-3 font-semibold">Privatnost</h3>
          <p class="mt-2 text-slate-700 leading-relaxed">Snimke i podaci ostaju tvoji.</p>
        </div>
      </div>
    </section>

    <!-- (donji CTA maknut) -->

    <!-- FOOTER TEAM -->
    <footer v-if="isHome" class="bg-gray-50 border-t py-10">
      <div class="max-w-6xl mx-auto px-6">
        <div class="flex flex-wrap justify-center gap-x-10 gap-y-6">
          <div v-for="member in teamSet" :key="member.name" class="text-center">
            <Avatar :image="member.url" class="medium lg:xlarge" shape="circle" />
            <div class="mt-2 font-medium">{{ member.name }}</div>
          </div>
        </div>
        <div class="mt-10 text-center text-xs text-slate-400">
          © {{ new Date().getFullYear() }} DailySpeakUp — Privacy • Contact • About
        </div>
      </div>
    </footer>
  </div>
</template>
