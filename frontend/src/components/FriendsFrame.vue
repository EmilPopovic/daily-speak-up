<script setup lang="ts">
  import ScrollPanel from 'primevue/scrollpanel';
  import Avatar from 'primevue/avatar';
</script>

<template>
  <div class="flex flex-row w-full h-full ">
        <ScrollPanel style="width: 100%; height: 100%">
          <div class="grid grid-cols-4 gap-4">
            <div v-for="i in 30" :key="i">

              <Avatar image="https://avatars.githubusercontent.com/u/236687211?v=4" class="mr-2" size="xlarge" shape="circle" :pt="{root:{class:'velicina_slike'}}" />
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
    width: 100%;
    height: auto;
    aspect-ratio: 1/1;
  }
</style>