<script setup lang="ts">
  import MainFrame from '../components/MainFrame.vue';
  import FriendsFrame from '../components/FriendsFrame.vue';
  import Divider from 'primevue/divider';
</script>

<template>
  <div class="flex flex-row w-full h-full">
    <MainFrame />
    <Divider layout="vertical" />
    <FriendsFrame />
  </div>
</template>

<style scoped>
.btnmy {
  --p-button-border-radius: 9rem;
}
</style>
