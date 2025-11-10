<script setup lang="ts">
import MainFrame from '../components/MainFrame.vue';
import FriendsFrame from '../components/FriendsFrame.vue';
</script>

<template>
  <div class="flex flex-row w-full h-full">
    <MainFrame />
    <FriendsFrame />
  </div>
</template>

<style scoped>
.btnmy {
  --p-button-border-radius: 9rem;
}
</style>
