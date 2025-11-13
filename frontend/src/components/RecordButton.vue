<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router'

// stanje
const progress = ref(0);
const isCounting = ref(false);
const showCancel = ref(false);

let intervalId = null;
const DURATION = 10_000; // 10 sekundi


const startTimer = () => {
  if (isCounting.value) return;

  isCounting.value = true;
  showCancel.value = true;
  progress.value = 0;
  const start = Date.now();

  intervalId = setInterval(() => {
    const elapsed = Date.now() - start;
    progress.value = Math.min(1, elapsed / DURATION);

    if (elapsed >= DURATION) {
      clearInterval(intervalId);
      progress.value = 1;
      isCounting.value = false;
      showCancel.value = false;
      generateTopic();
    }
  }, 1000 / 60);
};

// prekid timera i "sessiona"
const cancelTimer = () => {
  clearInterval(intervalId);
  isCounting.value = false;
  showCancel.value = false;
  progress.value = 0;
 
};

const generateTopic = async () => {
  try {
    const response = await fetch(BACKEND_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        interes: interes.value,
        lang: lang.value,
      }),
    });

    if (!response.ok) {
      throw new Error(`Greška: ${response.status}`);
    }

    const data = await response.json();
    console.log("Generirana tema:", data);
 
    const router = useRouter();
    router.push({ name: 'topics', query: { tema: data.tema, lang: data.lang } });

  } catch (error) {
    console.error("Greška pri pozivu /topics/generate:", error);
  }
};
</script>

<template>
  <div
    class="relative w-[30vw] h-[30vw] 2xl:w-[20vw] 2xl:h-[20vw] flex justify-center items-center mx-auto"
    @click="startTimer"
  >
    <!-- pozadina gumba -->
    <div
      class="absolute inset-0 rounded-full bg-gradient-to-b from-sky-200 to-sky-400 shadow-lg
             hover:cursor-pointer hover:scale-105 transition duration-300"
    ></div>

    <!-- plava kružnica (progress ring) -->
    <svg
      class="absolute w-full h-full -rotate-90"
      viewBox="0 0 100 100"
      xmlns="http://www.w3.org/2000/svg"
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

    <div class="pi pi-microphone z-10" style="color: white; font-size: 16vw"></div>

    <button
      v-if="showCancel"
      @click.stop="cancelTimer"
      class="absolute bottom-[-15%] w-16 h-16 rounded-full bg-red-600 shadow-lg
             hover:bg-red-700 transition text-white text-3xl flex items-center justify-center"
    >
      ✖
    </button>
  </div>
</template>

<style scoped>
</style>
