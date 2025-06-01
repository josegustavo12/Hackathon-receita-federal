// src/main.js

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// ui/ux
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'

// CSS global
import './assets/styles.css'

// Defina uma baseURL padrão para todas as requisições
axios.defaults.baseURL = 'localhost:8080' // ajuste conforme necessário

const app = createApp(App)

// Registra axios globalmente como this.$axios em todos os componentes
app.config.globalProperties.$axios = axios

app.use(router).mount('#app')