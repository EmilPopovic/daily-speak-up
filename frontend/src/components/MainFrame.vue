<script setup lang="ts">
import { ref, onMounted } from "vue";
import NavBar from "./NavBar.vue";
import RecordButton from "./RecordButton.vue";
import Fieldset from "primevue/fieldset";
 
const topic = ref<string | null>(null);
const interest = ref<string>("public speaking");
const lang = ref<string>("hr");


onMounted(async () => {
  try {
    const res = await fetch("http://localhost:8123/api/v1/userdata/interests");
    const data = await res.json();
    const randomIndex = Math.floor(Math.random() * data.interests.length);
    interest.value = data.interests[randomIndex];
    console.log("[MainFrame] fetched interests:", interest.value);
  } catch (error) {
    console.error("[MainFrame] failed to fetch interests:", error);
  }
});

// privremeno hardkodirano – kasnije možeš spojiti na prave vrijednosti

const handleTopicGenerated = (tema: string, generatedLang: string) => {
  console.log("[Page] topic-generated event:", tema, generatedLang);
  topic.value = tema;
  // lang.value = generatedLang; // ako želiš
};
</script>

<template>
  <div
    class="flex flex-col justify-start items-center bg-sky-100 w-[100vw] h-[60vh] lg:w-[65%] lg:h-full"
  >
    <NavBar />

    <div
      class="w-full h-[53vh] lg:h-full flex flex-col justify-around items-center "
    >
      <div
        class="border-black justify-center
                font-sans text-[1.5vw] font-semibold text-center"
      >
        <h1>Start practicing!</h1>
      </div>

      <div class="my-[5vh]">
        <RecordButton
          :interes="interest"
          :lang="lang"
          @topic-generated="handleTopicGenerated"
        />
      </div>

      <div>
        <Fieldset legend="Tema za govor" :toggleable="true">
          <p class="m-0" v-if="topic">
            {{ topic }}
          </p>
          <p class="m-0" v-else>
            Vaša će se tema za govor ovdje pojaviti nakon što pritisnete gumb
            za snimanje.
          </p>
        </Fieldset>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
