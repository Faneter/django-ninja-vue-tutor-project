<script setup>
import {ref} from "vue";

defineProps(['handler'])

const page = ref(1)

defineExpose({
  page,
})
</script>

<template>
  <button class="btn" @click="page--;handler()">上一页</button>
  第 {{ page }} 页
  <button class="btn" @click="page++;handler()">下一页</button>
</template>

<style scoped>

</style>