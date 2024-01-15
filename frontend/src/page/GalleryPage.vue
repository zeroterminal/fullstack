<template>    
    <v-container>
        <v-row class="text-center">
            <v-col cols="12">
                <v-img :src="logo" class="my-3" contain height="200" />
            </v-col>
            <v-col>
                
            </v-col>
            <v-col class="mb-4">
                <h1 class="display-2 font-weight-bold mb-3">
                    Welcome to the Gallery Page.
                </h1>
                <h4>Gallery </h4>
            </v-col>

            <v-col class="mb-5" cols="12">
                <h2 class="headline font-weight-bold mb-5">
                    Image
                </h2>
            </v-col>

            <v-col class="mb-5" cols="12">
                <h2 class="headline font-weight-bold mb-5">
                    Important Links
                </h2>

                <v-row justify="center">
                    <a v-for="(link, i) in importantLinks" :key="i" :href="link.href" class="subheading mx-3" target="_blank">
                        {{ link.text }}
                    </a>
                </v-row>
            </v-col>

            <v-col class="mb-5" cols="12">
                <h2 class="headline font-weight-bold mb-5">
                    Ecosystem
                </h2>

                <v-row justify="center">
                    <a v-for="(eco, i) in ecosystem" :key="i" :href="eco.href" class="subheading mx-3" target="_blank">
                        {{ eco.text }}
                    </a>
                </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import logo from '../assets/logo.svg'

export default {
    name: 'Gallery',

    data: () => ({
        logo,   
    }),
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300&display=swap');

.rubik {
    font-family: 'Rubik', sans-serif;
}

* {
    font-family: 'Rubik', sans-serif;
}
</style>
