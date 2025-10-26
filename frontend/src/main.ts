import App from './App.vue';
import { createApp } from 'vue';
import './style.css'
import PrimeVue from 'primevue/config';
import Lara from '@primeuix/themes/lara';

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: Lara,
        options: {
            darkModeSelector: false
        }
    }
});

app.mount('#app');