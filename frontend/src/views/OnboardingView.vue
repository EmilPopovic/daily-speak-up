<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { api } from '../api';
import Phase1 from '../components/Phase1.vue';
import Phase2 from '../components/Phase2.vue';

const router = useRouter();
const phase = ref<number | null>(null);
const loading = ref(true);

onMounted(async () => {
  const st = await api('/onboarding/state', { method: 'GET' });
  if (st.completed) return router.replace('/app');
  phase.value = st.phase;
  loading.value = false;
});

function onPhase1Done() { phase.value = 2; }
function onPhase2Done() { router.replace('/app'); }
</script>

<template>
  <div v-if="!loading" class="mx-auto max-w-2xl p-6">
    <div class="mb-6 flex gap-2">
      <span class="px-3 py-1 rounded" :class="phase! >= 1 ? 'bg-black text-white' : 'bg-gray-200'">1. Profil</span>
      <span class="px-3 py-1 rounded" :class="phase! >= 2 ? 'bg-black text-white' : 'bg-gray-200'">2. Interesi</span>
    </div>
    <Phase1 v-if="phase === 1" @done="onPhase1Done" />
    <Phase2 v-else-if="phase === 2" @done="onPhase2Done" />
  </div>
  <div v-else class="p-8">Učitavanje…</div>
</template>
