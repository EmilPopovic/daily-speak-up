<script setup lang="ts">
  import ScrollPanel from 'primevue/scrollpanel';
  import Avatar from 'primevue/avatar';
</script>

<template>
  <div class="flex flex-col w-[35%] h-full bg-linear-to-t from-slate-100 via-slate-50 to-slate-100 border-l-2
              border-slate-300 ">
    <div class="w-full flex flex-row justify-center items-center py-2 bg-linear-180 from-slate-200 to-slate-300 text-slate-600 font-semibold text-3xl py-4 ">
      <span class="pi pi-users mr-3" style="font-size: 2rem;"></span>
      Prijatelji
    </div>
    <ScrollPanel style="width: 99%; height: 93%">
      
      <div class="grid grid-cols-3 gap-3 mt-8  mr-5 ml-5">
        <div v-for="i in 30" :key="i" class="m-1">
          <Avatar image="https://avatars.githubusercontent.com/u/236687211?v=4" class="shadow-md" size="xlarge" shape="circle" :pt="{root:{class:'velicina_slike'}}" />
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