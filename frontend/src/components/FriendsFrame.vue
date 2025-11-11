<script setup lang="ts">
  import ScrollPanel from 'primevue/scrollpanel';
  import Avatar from 'primevue/avatar';
</script>

<template>
  <div class="flex flex-col w-[40%] h-full ">
    <div class="w-full py-2  bg-blue-50 text-sky-500 font-semibold text-2xl mt-8">
      Prijatelji
    </div>
    <ScrollPanel style="width: 99%; height: 100%">
      
      <div class="grid grid-cols-4 gap-4 mt-8" >
        <div v-for="i in 30" :key="i" class="m-1">

          <Avatar image="https://avatars.githubusercontent.com/u/236687211?v=4" class="" size="xlarge" shape="circle" :pt="{root:{class:'velicina_slike'}}" />
          <div>
            Lara D
          </div>
        </div>
        


        

      </div>
    </ScrollPanel>

  </div>
</template>

<style scoped>
  .velicina_slike{
    width: 85%;
    height: auto;
    aspect-ratio: 1/1;
  }
</style>