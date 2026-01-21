<script setup>
import request from "@/utils/request";
import {reactive, ref} from "vue";

const common_verification_information = reactive({
  id_card: '',
})

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

function parent_verification() {
  // 重置消息
  errorMessage.value = ''
  successMessage.value = ''

  // 验证身份证
  if (common_verification_information.id_card.length !== 18) {
    errorMessage.value = "请输入有效的身份证号码。"
    return;
  }

  isLoading.value = true

  request.post("/user/verify/parent", {
    id_card: common_verification_information.id_card,
  }).then((response) => {
    if (response.status === "success") {
      successMessage.value = "已提交认证！"
      setTimeout(() => {
        // 自动关闭模态框
        document.getElementById('verification_modal')?.close();
      }, 1500);
    } else {
      errorMessage.value = response.error_message || "认证失败，请重试"
    }
  }).catch((error) => {
    console.error("Register error:", error)
    errorMessage.value = "网络错误，请检查连接后重试"
  }).finally(() => {
    isLoading.value = false
  })
}

</script>

<template>
  <dialog id="verification_modal" class="modal modal-middle">
    <div class="modal-box max-w-md p-8">
      <!-- 关闭按钮 -->
      <form method="dialog" class="absolute right-4 top-4">
        <button class="btn btn-sm btn-circle btn-ghost">✕</button>
      </form>

      <!-- 标题 -->
      <h3 class="text-2xl font-bold text-center mb-8">身份认证</h3>

      <!-- 成功消息 -->
      <div v-if="successMessage"
           class="alert alert-success mb-6 animate-fade-in">
        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <span>{{ successMessage }}</span>
      </div>

      <!-- 错误消息 -->
      <div v-if="errorMessage"
           class="alert alert-error mb-6 animate-fade-in">
        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <span>{{ errorMessage }}</span>
      </div>

      <!-- 表单 -->
      <div class="tabs tabs-lift">
        <input type="radio" name="verification_tab" class="tab" aria-label="家长认证" checked="checked"/>
        <div class="tab-content bg-base-100 border-base-300 p-6 space-y-6">
          <!-- 用户名输入 -->
          <div class="form-control">
            <fieldset class="fieldset">
              <legend class="fieldset-legend">身份证</legend>
              <label class="input validator w-full">
                <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
                <input
                    v-model="common_verification_information.id_card"
                    type="text"
                    placeholder="请输入18位身份证号码"
                    required
                    minlength="18"
                    maxlength="18"
                    :disabled="isLoading"
                />
              </label>
              <p class="validator-hint hidden">身份证长度应为18个字符</p>
            </fieldset>

            <!-- 认证按钮 -->
            <div class="form-control mt-8">
              <button
                  @click="parent_verification"
                  class="btn btn-primary"
                  :class="{ 'loading': isLoading }"
                  :disabled="isLoading"
              >
                <span v-if="!isLoading">提交认证信息</span>
                <span v-else>提交信息中...</span>
              </button>
            </div>
          </div>
        </div>
        <input type="radio" name="verification_tab" class="tab" aria-label="家教认证"/>
        <div class="tab-content bg-base-100 border-base-300 p-6">家教认证</div>
      </div>
    </div>

    <!-- 模态框背景 -->
    <form method="dialog" class="modal-backdrop">
      <button :disabled="isLoading">关闭</button>
    </form>
  </dialog>
</template>

<style scoped>

</style>