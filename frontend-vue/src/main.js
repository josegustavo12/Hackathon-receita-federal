import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// ui/ux
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

// CSS global
import './assets/styles.css';

createApp(App).use(router).mount('#app')
