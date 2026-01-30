<script setup>
import request from "@/utils/request.js";
import Modal from "@/widget/Modal.vue";
import {reactive, ref} from "vue";

const props = defineProps(['id'])

const request_information = reactive({
  student_name: '',
  student_age: '',
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
    <div class="form-control flex gap-2">
      <!-- 学生姓名 -->
      <fieldset class="fieldset">
        <legend class="fieldset-legend">学生姓名</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
          <input
              v-model="request_information.student_name"
              type="text"
              placeholder="请输入学生姓名"
              required
              minlength="0"
              :disabled="isLoading"
          />
        </label>
        <p class="validator-hint hidden">请输入姓名</p>
      </fieldset>

      <!-- 学生年龄 -->
      <fieldset class="fieldset">
        <legend class="fieldset-legend">学生年龄</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2">
            <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          <input
              v-model="request_information.student_age"
              type="number"
              placeholder="请输入学生年龄"
              required
              min="0"
              :disabled="isLoading"
          />
        </label>
        <p class="validator-hint hidden">请输入有效的年龄</p>
      </fieldset>
    </div>

    <!-- 发布需求按钮 -->
    <div class="form-control mt-8">
      <button
          @click="publish_request"
          class="btn btn-primary"
          :class="{ 'loading': isLoading }"
          :disabled="isLoading"
      >
        <span v-if="!isLoading">发布</span>
        <span v-else>发布中...</span>
      </button>
    </div>
  </Modal>
</template>

<style scoped>

</style>