import { createApp } from 'vue'
// import router from './router/router'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()



// createApp(App)
//     .use(vuetify)
//     .use(router)
//     .mount('#app')

createApp(App)
    .use(vuetify)
    .mount('#app')