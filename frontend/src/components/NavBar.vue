<script setup>
    import AccountDrawer from './AccountDrawer.vue';
</script>

<template>

    <div class="flex flex-row justify-between items-center w-[95%] border border-gray-100
                mx-2 mt-8 rounded-full p-1 shadow-lg bg-blue-50">

        <div class="flex flex-row items-center ml-1">
            <img src="../assets/DSU_logo_circle.svg" alt="Daily Speak Up Logo" class="h-12 mr-3"/>
            <div class="text-sky-500 font-semibold text-3xl">DailySpeakUp</div>
        </div>

        <AccountDrawer />

    </div>
    
</template>

<style scoped>
</style>