<script setup>
import { ref, reactive } from 'vue'

const props = defineProps({
  character_data: Object,
  characters_length: Number,
  idx: Number
})

const character = ref(props.character_data)
const characters_length = ref(props.characters_length)
const characterd_idx = ref(props.idx)

function getLeftPad() {
  let div_char = characters_length.value/4

  if (characterd_idx.value <= div_char){
    console.log((50+((30/div_char)*(characterd_idx.value))))
    return (43+(36/div_char)*(characterd_idx.value))
  } else if (characterd_idx.value <= div_char*2) {
    return (80-(30/div_char)*(characterd_idx.value-div_char))
  } else if (characterd_idx.value <= div_char*3) {
    return (50-(30/div_char)*(characterd_idx.value-div_char*2))
  } else if (characterd_idx.value <= div_char*4) {
    return (15+(30/div_char)*(characterd_idx.value-div_char*3))
  }
}

function getTopPad() {
  let div_char = Math.floor(characters_length.value/2)

  if (characterd_idx.value <= div_char){
    return (67-(50/div_char)*(characterd_idx.value))
  } 
  return (7.5+(50/div_char)*(characterd_idx.value-div_char))
}

function getScale() {
  let div_char = Math.floor(characters_length.value/2)

  return 1 - (1/div_char*2)*characterd_idx.value
}

const styleObject = reactive({
  top: `${getTopPad()}%`,
  left: `${getLeftPad()}%`,
  transform: `scale(${getScale()})`,
  "z-index": 1000-characterd_idx.value
})
</script>

<template>
    <div :style="styleObject">
        <img :src="character_data.image_url" alt="">
    </div>
</template>

<style scoped>
img { 
  max-width: 100%;
  max-height: 100%;
}
</style>
