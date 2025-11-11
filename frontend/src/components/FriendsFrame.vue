<script setup lang="ts">
  import ScrollPanel from 'primevue/scrollpanel';
  import Avatar from 'primevue/avatar';
</script>

<template>
  <div class="flex flex-col w-[35%] h-full bg-slate-100 ">
    <div class="w-full py-2  bg-slate-200 text-slate-600 font-semibold text-2xl">
      Prijatelji
    </div>
    <ScrollPanel style="width: 99%; height: 93%">
      
      <div class="grid grid-cols-3 gap-3 mt-8  mr-5 ml-5">
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
  .skrol_panel{
    --p-scrollpanel-bar-background: red;
  }
</style>