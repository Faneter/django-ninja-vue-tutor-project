<script setup>
import request from "@/utils/request";
import {reactive, ref} from "vue";

import Modal from "@/components/Modal.vue";

const login_information = reactive({
  phone: '',
  password: '',
})

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

function login() {
  // 重置消息
  errorMessage.value = ''
  successMessage.value = ''

  // 前端验证
  if (!login_information.phone.match(/^1[3-9]\d{9}$/)) {
    errorMessage.value = '请输入有效的手机号码'
    return
  }

  isLoading.value = true

  request.post(`/user/login`, {
    phone: login_information.phone,
    password: login_information.password,
  }).then(response => {
    if (response.status === "success") {
      successMessage.value = "登录成功！"
      location.reload(true)
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
  <Modal :id="$attrs.id" title="用户登录" :successMessage="successMessage" :errorMessage="errorMessage"
         :isLoading="isLoading">
    <!-- 手机号输入 -->
    <div class="form-control">
      <fieldset class="fieldset">
        <legend class="fieldset-legend">手机号</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
            <g fill="none">
              <path
                  d="M7.25 11.5C6.83579 11.5 6.5 11.8358 6.5 12.25C6.5 12.6642 6.83579 13 7.25 13H8.75C9.16421 13 9.5 12.6642 9.5 12.25C9.5 11.8358 9.16421 11.5 8.75 11.5H7.25Z"
                  fill="currentColor"></path>
              <path fill-rule="evenodd" clip-rule="evenodd"
                    d="M6 1C4.61929 1 3.5 2.11929 3.5 3.5V12.5C3.5 13.8807 4.61929 15 6 15H10C11.3807 15 12.5 13.8807 12.5 12.5V3.5C12.5 2.11929 11.3807 1 10 1H6ZM10 2.5H9.5V3C9.5 3.27614 9.27614 3.5 9 3.5H7C6.72386 3.5 6.5 3.27614 6.5 3V2.5H6C5.44771 2.5 5 2.94772 5 3.5V12.5C5 13.0523 5.44772 13.5 6 13.5H10C10.5523 13.5 11 13.0523 11 12.5V3.5C11 2.94772 10.5523 2.5 10 2.5Z"
                    fill="currentColor"></path>
            </g>
          </svg>
          <input
              v-model="login_information.phone"
              type="tel"
              class="tabular-nums"
              placeholder="请输入11位手机号"
              required
              maxlength="11"
              :disabled="isLoading"
          />
        </label>
        <p class="validator-hint hidden">手机号格式不正确</p>
      </fieldset>
    </div>

    <!-- 密码输入 -->
    <div class="form-control">
      <fieldset class="fieldset">
        <legend class="fieldset-legend">密码</legend>
        <label class="input validator w-full">
          <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <g
                stroke-linejoin="round"
                stroke-linecap="round"
                stroke-width="2.5"
                fill="none"
                stroke="currentColor"
            >
              <path
                  d="M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z"
              ></path>
              <circle cx="16.5" cy="7.5" r=".5" fill="currentColor"></circle>
            </g>
          </svg>
          <input
              v-model="login_information.password"
              type="password"
              required
              placeholder="密码"
              minlength="8"
              pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
              title="至少8个字符，至少包括一个数字、一个大写字母、一个小写字母"
              :disabled="isLoading"
          />
        </label>
        <p class="validator-hint hidden">
          至少8个字符，包括一个数字、大写字母、小写字母
        </p>
      </fieldset>
    </div>

    <!-- 登录按钮 -->
    <div class="form-control mt-8">
      <button
          @click="login"
          class="btn btn-primary"
          :class="{ 'loading': isLoading }"
          :disabled="isLoading"
      >
        <span v-if="!isLoading">登录</span>
        <span v-else>登录中...</span>
      </button>
    </div>
  </Modal>
</template>

<style scoped>
</style>