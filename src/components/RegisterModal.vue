<script setup>
import request from "@/utils/request";
import {reactive, ref} from "vue";

const register_information = reactive({
  phone: '',
  password: '',
  confirm_password: '',
})

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

function register() {
  // 重置消息
  errorMessage.value = ''
  successMessage.value = ''

  if (!register_information.phone.match(/^1[3-9]\d{9}$/)) {
    errorMessage.value = '请输入有效的手机号码'
    return;
  }

  if (!register_information.password.match(/(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/)) {
    errorMessage.value = '密码至少8个字符，至少包括一个数字、一个大写字母、一个小写字母'
  }

  if (register_information.password !== register_information.confirm_password) {
    errorMessage.value = '两次输入的密码不一致'
    return;
  }

  isLoading.value = true

  request.post("/api/user/register", {
    phone: register_information.phone,
    password: register_information.password,
  }).then((response) => {
    console.log(response)
    if (response.status === "success") {
      successMessage.value = "登录成功！"
      location.reload(true)
    } else {
      errorMessage.value = response.error_message || "注册失败，请重试"
    }
  }).catch(error => {
    console.error("Register error:", error)
    errorMessage.value = "网络错误，请检查连接后重试"
  }).finally(() => {
    isLoading.value = false
  })
}
</script>

<template>

</template>

<style scoped>

</style>