import { createRouter, createWebHistory } from 'vue-router'
import Home from "../page/HomePage.vue";
import Gallery from "../page/GalleryPage.vue";



const routes = [
    { path: '/', component: Home },
    { path: '/gallery', component: Gallery },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;