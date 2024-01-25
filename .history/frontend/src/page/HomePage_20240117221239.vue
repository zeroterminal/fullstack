<style scoped>
body {
    background: #222;
}

@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap');

.rubik {
    font-family: 'Rubik', sans-serif;
}

* {
    font-family: 'Rubik', sans-serif;
}
</style>

<template>
    <v-container>
        <v-row class="text-center">
            <v-col cols="12">
                <v-img :src="logo" class="my-3" contain height="200" />
            </v-col>

            <v-col class="mb-4">
                <h1 class="display-2 font-weight-bold mb-3">
                    Welcome to the Home Page
                </h1>
                <h4>HOME</h4>
            </v-col>

            <v-col class="mb-5" cols="12">
                <h2 class="headline font-weight-bold mb-5">
                    <a v-for="(link, i) in links" :key="i" :href="link.href" class="subheading mx-3" target="_blank">
                        {{ link.text }}
                    </a>
                </h2>
            </v-col>

            <v-col class="mb-5" cols="12">
                
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import logo from '../assets/logo.svg'

export default {
    name: 'Home',

    data: () => ({
        logo,
        importantLinks: [
            { text: 'HOME', href: '/', },
            { text: 'GALLERY', href: '/gallery', },
            { text: 'Twitter', href: '/', },
            { text: 'Articles', href: '/', },
        ],
    }),
}
</script>
