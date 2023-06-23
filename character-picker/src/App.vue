<script setup>
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import Character from './components/Character.vue';

fetch('./characters.json')
  .then((response) => response.json())
  .then((json) => characters.value = json)

const characters = ref(null)

function getPadding(idx) {
  let left_pad = 100 / characters.length
  return `${left_pad}vw`
}
</script>

<template>
  <div class="container">
    <Character class="character-slot" :idx="idx" :characters_length="characters.length" :character_data="character" v-for="character, idx in characters" :key="idx" />
  </div>
</template>

<style scoped>
.container {
  display: flex;
  height: 100%;
  width: 100%;
  justify-items: center;
  align-items: center;
  overflow: hidden;
}
.character-slot {
  position: absolute;
  width: 200px;
  height: 300px;
}
</style>
