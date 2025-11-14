<script setup lang="ts">
import { computed } from 'vue';

const environment = computed(() => {
  const env = import.meta.env.VITE_ENVIRONMENT || 
               (window as any).ENV?.VITE_ENVIRONMENT || 
               import.meta.env.MODE || 
               'development';
  
  return env.toLowerCase();
});

const showIndicator = computed(() => {
  const env = environment.value;
  return env !== 'prod' && env !== 'production';
});

const indicatorConfig = computed(() => {
  const env = environment.value;
  
  if (env === 'development' || env === 'dev') {
    return {
      color: 'bg-yellow-500',
      label: 'DEV',
      fullLabel: 'Development'
    };
  } else if (env === 'staging' || env === 'stage') {
    return {
      color: 'bg-blue-500',
      label: 'STAGING',
      fullLabel: 'Staging'
    };
  } else if (env === 'test' || env === 'testing') {
    return {
      color: 'bg-purple-500',
      label: 'TEST',
      fullLabel: 'Testing'
    };
  } else {
    return {
      color: 'bg-orange-500',
      label: env.toUpperCase(),
      fullLabel: env.charAt(0).toUpperCase() + env.slice(1)
    };
  }
});
</script>

<template>
  <div 
    v-if="showIndicator"
    class="fixed top-0 left-0 pointer-events-none"
    style="z-index: 9999;"
  >
    <div 
      :class="[
        'px-3 py-1.5 text-white font-bold text-xs shadow-lg',
        'flex items-center gap-2',
        indicatorConfig.color
      ]"
      style="border-bottom-right-radius: 0.5rem;"
      :title="`Environment: ${indicatorConfig.fullLabel}`"
    >
      <span class="inline-block w-2 h-2 bg-white rounded-full animate-pulse"></span>
      <span>{{ indicatorConfig.label }}</span>
    </div>
  </div>
</template>

<style scoped>
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
</style>
