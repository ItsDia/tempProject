import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)
app.use(router)
app.use(VueAxios, axios)
app.use(ElementPlus)
axios.defaults.baseURL = "http://localhost:5173/" // 设置默认请求的基础 URL
axios.defaults.timeout = 10000 // 请求超时时间
app.config.globalProperties.$axios = axios // 将 Axios 挂载到 Vue 实例的全局属性中
app.mount('#app')
