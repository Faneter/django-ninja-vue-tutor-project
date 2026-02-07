<script setup>
import {ref} from "vue";

const props = defineProps(['page_num', 'handler'])

const page = ref(1)

function increasePage() {
  page.value = page.value < props.page_num ? page.value + 1 : page.value
  props.handler(page.value)
}

function decreasePage() {
  page.value = page.value > 1 ? page.value - 1 : page.value
  props.handler(page.value)
}

defineExpose({
  page,
})
</script>

<template>
  <div class="flex justify-center items-center w-full">
    <button class="btn" @click="increasePage">上一页</button>
    第 {{ page }} 页
    <button class="btn" @click="decreasePage">下一页</button>
  </div>
</template>

<style scoped>

</style>