<script setup>
import request from "@/utils/request.js";
import {reactive, ref} from "vue";

const verification_status = ref("");

const button_text = reactive({
  main: "身份认证",
  sub: "",
})

const button_sub_text_style = ref("")

const not_verifiable = ref(true)

function get_verification_status() {
  request.get("/user/verify/status").then(response => {
    verification_status.value = response.status;
  }).catch(error => {
    console.log(error)
    verification_status.value = "ERROR"
  }).finally(() => {
    switch (verification_status.value) {
      case "NONE":
        button_text.main = "身份认证"
        button_text.sub = "去认证"
        not_verifiable.value = false
        button_sub_text_style.value = "badge-info"
        break
      case "WAITING":
        button_text.main = "身份认证"
        button_text.sub = "审核中"
        not_verifiable.value = true
        button_sub_text_style.value = "badge-neutral"
        break
      case "FAILED":
        button_text.main = "身份认证"
        button_text.sub = "认证失败"
        not_verifiable.value = false
        button_sub_text_style.value = "badge-error"
        break
      case "PARENT":
        button_text.main = "已认证"
        button_text.sub = "家长"
        not_verifiable.value = true
        button_sub_text_style.value = "badge-success"
        break
      case "TUTOR":
        button_text.main = "已认证"
        button_text.sub = "家教"
        not_verifiable.value = true
        button_sub_text_style.value = "badge-success"
        break
      case "ERROR":
        button_text.main = "身份认证"
        button_text.sub = "错误"
        not_verifiable.value = true
        button_sub_text_style.value = "badge-error"
        break
      default:
        button_text.main = "身份认证"
        button_text.sub = "错误"
        not_verifiable.value = true
        button_sub_text_style.value = "badge-error"
        break
    }
  })
}

get_verification_status()

</script>

<template>
  <button class="justify-between" onclick="verification_modal.showModal()" :disabled="not_verifiable">
    {{ button_text.main }}
    <span class="badge" v-bind:class="button_sub_text_style">
      {{ button_text.sub }}
    </span>
  </button>
</template>

<style scoped>

</style>