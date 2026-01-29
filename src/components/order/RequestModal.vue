<script setup>
import request from "@/utils/request.js";
import Modal from "@/widget/Modal.vue";
import {reactive, ref} from "vue";

const props = defineProps(['id'])

const request_information = reactive({
  student_name: 'TEST',
  student_age: 7,
  student_gender: 'M',
  student_grade: 'P1',

  subject: 'CHI',
  experienced: false,

  method: 'T',
  tutor_gender: 'F',

  lesson_date: 'str',
  lesson_time: 'str',
  lesson_days: 20,

  payment_type: 'D',
  salary: 200,
})

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

function publish_request() {
  // 重置消息
  errorMessage.value = ''
  successMessage.value = ''

  isLoading.value = true

  request.post(`/order/create`, {
    student_name: request_information.student_name,
    student_age: request_information.student_age,
    student_grade: request_information.student_grade,
    student_gender: request_information.student_gender,
    subject: request_information.subject,
    experienced: request_information.experienced,
    method: request_information.method,
    tutor_gender: request_information.tutor_gender,
    lesson_date: request_information.lesson_date,
    lesson_time: request_information.lesson_time,
    lesson_days: request_information.lesson_days,
    payment_type: request_information.payment_type,
    salary: request_information.salary,
  }).then(response => {
    if (response.status === "success") {
      successMessage.value = "发布成功！"
      setTimeout(() => {
        document.getElementById(`${props.id}`)?.close();
      }, 1500);
    } else {
      errorMessage.value = response.error_message || "登录失败，请重试"
    }
  }).catch(error => {
    console.error("Login error:", error)
    errorMessage.value = "网络错误，请检查连接后重试"
  }).finally(() => {
    isLoading.value = false
  })
}

</script>

<template>
  <Modal :id="props.id" title="发布需求" :successMessage="successMessage" :errorMessage="errorMessage"
         :isLoading="isLoading">
    <!-- 发布需求按钮 -->
    <div class="form-control mt-8">
      <button
          @click="publish_request"
          class="btn btn-primary"
          :class="{ 'loading': isLoading }"
          :disabled="isLoading"
      >
        <span v-if="!isLoading">发布需求</span>
        <span v-else>发布中...</span>
      </button>
    </div>
  </Modal>
</template>

<style scoped>

</style>