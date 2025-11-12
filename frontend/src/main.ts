import App from './App.vue';
import { createApp } from 'vue';
import './style.css'
import PrimeVue from 'primevue/config';
import Lara from '@primeuix/themes/lara';
import { definePreset } from '@primeuix/themes';
import router from './router';
import { initSuperTokens } from './supertokens';

const DailySpeakUpPreset = definePreset(Lara, {
    semantic: {
        primary: {
            50: '{sky.50}',
            100: '{sky.100}',
            200: '{sky.200}',
            300: '{sky.300}',
            400: '{sky.400}',
            500: '{sky.500}',
            600: '{sky.600}',
            700: '{sky.700}',
            800: '{sky.800}',
            900: '{sky.900}',
            950: '{sky.950}'
        },
    }
});

// Initialize SuperTokens
initSuperTokens();

const app = createApp(App);

// middleware
app.use(PrimeVue, {
    theme: {
        preset: DailySpeakUpPreset,
        options: {
            darkModeSelector: false
        }
    }
});

app.use(router);

app.mount('#app');