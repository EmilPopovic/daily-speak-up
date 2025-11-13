<script setup>
import { ref, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router";

const progress = ref(0);
const isCounting = ref(false);

let intervalId = null;
const DURATION = 10_000;

const router = useRouter();

const startTimer = () => {
  if (isCounting.value) return;

  isCounting.value = true;
  progress.value = 0;
  const start = Date.now();

  intervalId = setInterval(() => {
    const elapsed = Date.now() - start;
    progress.value = Math.min(1, elapsed / DURATION);

    if (elapsed >= DURATION) {
      clearInterval(intervalId);
      intervalId = null;
      progress.value = 1;
      isCounting.value = false;

      generateTopic();
    }
  }, 1000 / 60);
};

const cancelTimer = () => {
  if (intervalId !== null) {
    clearInterval(intervalId);
    intervalId = null;
  }
  isCounting.value = false;
  progress.value = 0;
};

onBeforeUnmount(() => {
  if (intervalId !== null) clearInterval(intervalId);
});

const generateTopic = async () => {
  try {
    const response = await fetch(BACKEND_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        interes: interes.value,
        lang: lang.value,
      }),
    });

    if (!response.ok) throw new Error(`Greška: ${response.status}`);

    const data = await response.json();

    router.push({
      name: "topics",
      query: { tema: data.tema, lang: data.lang },
    });

  } catch (error) {
    console.error("Greška pri pozivu /topics/generate:", error);
  }
};
</script>

<template>
  <div class="relative flex justify-center items-center mx-auto">

    <!-- Krug sa hover efektom koji ga samo potamni -->
    <div
      class="w-[22vw] h-[22vw] 2xl:w-[16vw] 2xl:h-[16vw] rounded-full
             bg-[radial-gradient(circle,_#c4eafe,_#38bdf8)]
             shadow-lg flex items-center justify-center
             hover:cursor-pointer transition-all duration-200
             hover:brightness-90"
      @click="isCounting ? cancelTimer() : startTimer()"
    >
      <!-- Mikrofon -->
      <span
        v-if="!isCounting"
        class="pi pi-microphone text-white"
        style="font-size: 9vw;"
      ></span>

      <!-- X za prekid -->
      <span
        v-else
        class="text-white"
        style="font-size: 9vw;"
        @click.stop="cancelTimer"
      >
        ✖
      </span>
    </div>

    <!-- Progress ring -->
    <svg
      v-if="isCounting"
      class="absolute w-full h-full -rotate-90 pointer-events-none"
      viewBox="0 0 100 100"
    >
      <circle
        cx="50"
        cy="50"
        r="48"
        stroke="#38bdf8"
        stroke-width="4"
        fill="none"
        stroke-dasharray="301.59"
        :stroke-dashoffset="301.59 - 301.59 * progress"
        class="transition-all duration-100"
      />
    </svg>
  </div>
</template>

<style scoped>
</style>
