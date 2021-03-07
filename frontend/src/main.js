import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from "@/store";
import axios from 'axios'
import VueAxios from 'vue-axios'


createApp(App).use(router).use(store).use(VueAxios, axios).mount('#app')

//const app = createApp(App).use(VueAxios, axios).mount('#app')



//app.use(store)