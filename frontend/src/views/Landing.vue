<script setup>
import Avatar from 'primevue/avatar';
import { ref } from 'vue';

const teamSet = ref([
    {url: 'https://avatars.githubusercontent.com/u/205453688?v=4', name: 'Lara Brečić'},
    {url: 'https://avatars.githubusercontent.com/u/236687211?v=4', name: 'Lara Desnica'},
    {url: 'https://avatars.githubusercontent.com/u/219036118?v=4', name: 'Mate Jakovljev'},
    {url: 'https://avatars.githubusercontent.com/u/153128323?v=4', name: 'Nika Valić'},
    {url: 'https://avatars.githubusercontent.com/u/104315710?v=4', name: 'Emil Popović'},
    {url: 'https://avatars.githubusercontent.com/u/74995193?v=4', name: 'Matej Jurasić'},
    {url: 'https://avatars.githubusercontent.com/u/44684310?v=4', name: 'Kristijan Bilanović'},
]);
</script>

<template>

    <div class="flex flex-row">
        <div v-for="(member, i) in teamSet" :key="i" class="ml-5 mr-5 ">
            <Avatar :image="member.url" class="mr-2" size="xlarge" shape="circle" />
            <div class="text-center mt-2">{{ member.name }}</div>
        </div>
    </div>

</template>