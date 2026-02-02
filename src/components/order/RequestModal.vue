<script setup>
import request from "@/utils/request.js";
import Modal from "@/widget/Modal.vue";
import {reactive, ref} from "vue";

const props = defineProps(['id'])

const request_information = reactive({
  student_name: '',
  student_age: '',
  student_gender: '',
  student_grade: '',

  subject: '',
  experienced: false,

  method: '',
  tutor_gender: '',

  lesson_date: '',
  lesson_time: '',
  lesson_days: '',

  payment_type: '',
  salary: '',
})

const gradeOptions = [
  {value: 'P1', label: '一年级'},
  {value: 'P2', label: '二年级'},
  {value: 'P3', label: '三年级'},
  {value: 'P4', label: '四年级'},
  {value: 'P5', label: '五年级'},
  {value: 'P6', label: '六年级'},
  {value: 'J1', label: '初一'},
  {value: 'J2', label: '初二'},
  {value: 'J3', label: '初三'},
  {value: 'S1', label: '高一'},
  {value: 'S2', label: '高二'},
  {value: 'S3', label: '高三'}
]

const subjectOptions = [
  {value: 'CHI', label: '语文'},
  {value: 'MAT', label: '数学'},
  {value: 'ENG', label: '英语'},
  {value: 'PHI', label: '物理'},
  {value: 'CHE', label: '化学'},
  {value: 'BIO', label: '生物'},
  {value: 'POL', label: '政治'},
  {value: 'HIS', label: '历史'},
  {value: 'GEO', label: '地理'}
]

const methodOptions = [
  {value: 'T', label: '学员上门'},
  {value: 'S', label: '家教上门'},
  {value: 'O', label: '线上辅导'}
]

const paymentOptions = [
  {value: 'D', label: '按天收费'},
  {value: 'H', label: '按小时收费'},
  {value: 'C', label: '面议'}
]

const genderOptions = [
  {value: 'M', label: '男'},
  {value: 'F', label: '女'},
]

const tutorGenderOptions = [
  {value: 'M', label: '男'},
  {value: 'F', label: '女'},
  {value: 'U', label: '不限'},
]

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

function publish_request() {
  // 重置消息
  errorMessage.value = ''
  successMessage.value = ''

  // 基本验证
  if (!request_information.student_name.trim()) {
    errorMessage.value = '请输入学生姓名'
    return
  }

  if (!request_information.student_age || request_information.student_age < 3) {
    errorMessage.value = '请输入有效的年龄'
    return
  }

  if (!request_information.student_gender) {
    errorMessage.value = '请选择性别'
    return;
  }

  if (!request_information.student_grade) {
    errorMessage.value = '请选择年级'
    return;
  }

  if (!request_information.subject) {
    errorMessage.value = '请选择科目'
    return;
  }

  if (!request_information.tutor_gender) {
    errorMessage.value = '请选择家教性别'
    return;
  }

  if (!request_information.method) {
    errorMessage.value = '请选择辅导方式'
    return;
  }


  if (!request_information.lesson_date) {
    errorMessage.value = '请输入辅导日期'
    return
  }

  if (!request_information.lesson_time) {
    errorMessage.value = '请输入辅导时间'
    return
  }

  if (!request_information.lesson_days) {
    errorMessage.value = '请输入辅导天数'
    return;
  }

  if (!request_information.payment_type) {
    errorMessage.value = '请选择支付方式'
    return;
  }

  if (!request_information.salary) {
    errorMessage.value = '请输入薪资'
    return;
  }

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
              min="3"
              :disabled="isLoading"
          />
        </label>
        <p class="validator-hint hidden">请输入有效的年龄</p>
      </fieldset>
    </div>
    <div class="form-control flex gap-2">
      <!-- 学生性别 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">学生性别</legend>
        <select class="select" v-model="request_information.student_gender" :disabled="isLoading">
          <option value="" disabled selected>选择性别</option>
          <option v-for="option in genderOptions" :value="option.value">{{ option.label }}</option>
        </select>
      </fieldset>
      <!-- 学生年级 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">学生年级</legend>
        <select class="select" v-model="request_information.student_grade" :disabled="isLoading">
          <option value="" disabled selected>选择年级</option>
          <option v-for="option in gradeOptions" :value="option.value">{{ option.label }}</option>
        </select>
      </fieldset>
    </div>
    <div class="form-control flex gap-2">
      <!-- 辅导科目 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">辅导科目</legend>
        <select class="select" v-model="request_information.subject" :disabled="isLoading">
          <option value="" disabled selected>选择科目</option>
          <option v-for="option in subjectOptions" :value="option.value">{{ option.label }}</option>
        </select>
      </fieldset>
      <!-- 是否有基础 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">是否有基础</legend>
        <div class="flex items-center space-x-4 mt-2">
          <label class="label cursor-pointer space-x-2">
            <input
                type="radio"
                v-model="request_information.experienced"
                :value="false"
                class="radio"
                :disabled="isLoading"
            />
            <span class="label-text">无基础</span>
          </label>
          <label class="label cursor-pointer space-x-2">
            <input
                type="radio"
                v-model="request_information.experienced"
                :value="true"
                class="radio"
                :disabled="isLoading"
            />
            <span class="label-text">有基础</span>
          </label>
        </div>
      </fieldset>
    </div>
    <div class="form-control flex gap-2">
      <!-- 家教性别 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">家教性别</legend>
        <select class="select" v-model="request_information.tutor_gender" :disabled="isLoading">
          <option value="" disabled selected>选择性别</option>
          <option v-for="option in tutorGenderOptions" :value="option.value">{{ option.label }}</option>
        </select>
      </fieldset>
      <!-- 辅导方式 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">辅导方式</legend>
        <select class="select" v-model="request_information.method" :disabled="isLoading">
          <option value="" disabled selected>选择方式</option>
          <option v-for="option in methodOptions" :value="option.value">{{ option.label }}</option>
        </select>
      </fieldset>
    </div>

    <!-- 辅导日期 -->
    <div class="form-control">
      <fieldset class="fieldset">
        <legend class="fieldset-legend">辅导日期</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50"
               xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
          </svg>
          <input
              v-model="request_information.lesson_date"
              type="text"
              placeholder="例：每周周六"
              required
              minlength="0"
              :disabled="isLoading"
          />
        </label>
      </fieldset>
    </div>
    <div class="form-control flex gap-2">
      <!-- 单次辅导时间 -->
      <fieldset class="fieldset w-3/5">
        <legend class="fieldset-legend">单次辅导时间</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50"
               xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <input
              v-model="request_information.lesson_time"
              type="text"
              placeholder="例：15:00-17:00"
              required
              minlength="0"
              :disabled="isLoading"
          />
        </label>
      </fieldset>

      <!-- 辅导天数 -->
      <fieldset class="fieldset w-2/5">
        <legend class="fieldset-legend">辅导天数</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <input
              v-model="request_information.lesson_days"
              type="number"
              placeholder="辅导天数"
              required
              min="0"
              :disabled="isLoading"
          />
        </label>
      </fieldset>
    </div>
    <div class="form-control flex gap-2">
      <!-- 付款方式 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">付款方式</legend>
        <select class="select" v-model="request_information.payment_type" :disabled="isLoading">
          <option value="" disabled selected>选择付款方式</option>
          <option v-for="option in paymentOptions" :value="option.value">{{ option.label }}</option>
        </select>
      </fieldset>

      <!-- 薪资 -->
      <fieldset class="fieldset w-full">
        <legend class="fieldset-legend">薪资(元)</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
               stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <input
              v-model="request_information.salary"
              type="number"
              placeholder="请输入薪资"
              required
              min="0"
              :disabled="isLoading"
          />
        </label>
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