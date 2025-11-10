import App from './App.vue';
import { createApp } from 'vue';
import './style.css'
import PrimeVue from 'primevue/config';
import Lara from '@primeuix/themes/lara';
import { definePreset } from '@primeuix/themes';
import router from './router';
import { createAuth0 } from '@auth0/auth0-vue';
import 'primeicons/primeicons.css'

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

const env = {
    VITE_AUTH0_DOMAIN: import.meta.env.VITE_AUTH0_DOMAIN || (window as any).ENV?.VITE_AUTH0_DOMAIN,
    VITE_AUTH0_CLIENT_ID: import.meta.env.VITE_AUTH0_CLIENT_ID || (window as any).ENV?.VITE_AUTH0_CLIENT_ID,
};

app.use(
    createAuth0({
        domain: env.VITE_AUTH0_DOMAIN,
        clientId: env.VITE_AUTH0_CLIENT_ID,
        authorizationParams: {
            redirect_uri: window.location.origin,
        },
        cacheLocation: "localstorage",
        useRefreshTokens: true,
    })
);

app.use(router);

app.mount('#app');