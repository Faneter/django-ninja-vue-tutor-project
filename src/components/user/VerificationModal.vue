<script setup>
import request from "@/utils/request";
import {reactive, ref} from "vue";

// 家长认证信息
const parent_verification_information = reactive({
  id_card: '',
})

// 家教认证信息
const tutor_verification_information = reactive({
  id_card: '',
  college_entrance_score: '',
  student_card: null,
  teacher_qualification_certificate: null,
})

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

// 处理文件选择
function handleStudentCardSelect(event) {
  const file = event.target.files[0]
  if (file) {
    if (!file.type.startsWith('image/')) {
      errorMessage.value = '请选择图片文件作为学生证'
      return
    }
    if (file.size > 1024 * 1024) { // 5MB限制
      errorMessage.value = '文件大小不能超过1MB'
      return
    }
    tutor_verification_information.student_card = file
  }
}

function handleTeacherCertificateSelect(event) {
  const file = event.target.files[0]
  if (file) {
    if (!file.type.startsWith('image/')) {
      errorMessage.value = '请选择图片文件作为教师资格证'
      return
    }
    if (file.size > 1024 * 1024) { // 5MB限制
      errorMessage.value = '文件大小不能超过1MB'
      return
    }
    tutor_verification_information.teacher_qualification_certificate = file
  }
}

// 移除已选择的文件
function removeStudentCard() {
  tutor_verification_information.student_card = null
  document.getElementById('student_card_input').value = ''
}

function removeTeacherCertificate() {
  tutor_verification_information.teacher_qualification_certificate = null
  document.getElementById('teacher_certificate_input').value = ''
}

function parent_verification() {
  // 重置消息
  errorMessage.value = ''
  successMessage.value = ''

  // 验证身份证
  if (parent_verification_information.id_card.length !== 18) {
    errorMessage.value = "请输入有效的身份证号码。"
    return;
  }

  isLoading.value = true

  request.post("/user/verify/parent", {
    id_card: parent_verification_information.id_card,
  }).then((response) => {
    if (response.status === "success") {
      successMessage.value = response.message || "已提交认证！"
      setTimeout(() => {
        // 重载页面刷新状态
        location.reload(true)
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

async function tutor_verification() {
  // 重置消息
  errorMessage.value = ''
  successMessage.value = ''

  // 验证身份证
  if (tutor_verification_information.id_card.length !== 18) {
    errorMessage.value = "请输入有效的身份证号码。"
    return;
  }

  // 验证高考成绩
  const score = parseInt(tutor_verification_information.college_entrance_score)
  if (isNaN(score) || score < 0 || score > 750) {
    errorMessage.value = "请输入有效的高考成绩（0-750）"
    return;
  }

  // 验证学生证
  if (!tutor_verification_information.student_card) {
    errorMessage.value = "请上传学生证照片"
    return;
  }

  isLoading.value = true

  try {
    // 构建FormData - 字段名称必须与API参数名称匹配
    const formData = new FormData()
    formData.append('id_card', tutor_verification_information.id_card)
    formData.append('college_entrance_score', score.toString())
    formData.append('student_card', tutor_verification_information.student_card)

    if (tutor_verification_information.teacher_qualification_certificate) {
      formData.append('teacher_qualification_certificate',
          tutor_verification_information.teacher_qualification_certificate)
    }

    console.log('Sending FormData with fields:', {
      id_card: tutor_verification_information.id_card,
      college_entrance_score: score,
      student_card: tutor_verification_information.student_card?.name,
      teacher_qualification_certificate: tutor_verification_information.teacher_qualification_certificate?.name
    })

    // 使用正确的API路径
    const response = await fetch('/api/user/verify/tutor', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
      },
      credentials: 'include',
    })

    console.log('Response status:', response.status)

    if (response.status === 200) {
      const data = await response.json()
      if (data.status === "success") {
        successMessage.value = data.message || "已提交家教认证！"
        setTimeout(() => {
          location.reload(true)
        }, 1500);
      } else {
        errorMessage.value = data.error_message || "认证失败，请重试"
      }
    } else {
      const errorText = await response.text()
      console.error('Server error:', errorText)
      errorMessage.value = `服务器错误: ${response.status} - ${errorText}`
    }
  } catch (error) {
    console.error("Tutor verification error:", error)
    errorMessage.value = "网络错误，请检查连接后重试"
  } finally {
    isLoading.value = false
  }
}

// 获取CSRF token的辅助函数
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
</script>

<template>
  <dialog id="verification_modal" class="modal modal-middle">
    <div class="modal-box max-w-md p-6">
      <!-- 关闭按钮 -->
      <form method="dialog" class="absolute right-4 top-4">
        <button class="btn btn-sm btn-circle btn-ghost">✕</button>
      </form>

      <!-- 标题 -->
      <h3 class="text-2xl font-bold text-center mb-6">身份认证</h3>

      <!-- 成功消息 -->
      <div v-if="successMessage"
           class="alert alert-success mb-4 animate-fade-in">
        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <span>{{ successMessage }}</span>
      </div>

      <!-- 错误消息 -->
      <div v-if="errorMessage"
           class="alert alert-error mb-4 animate-fade-in">
        <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
        <span>{{ errorMessage }}</span>
      </div>

      <!-- 标签页 -->
      <div class="tabs tabs-lift">
        <input type="radio" name="verification_tab" class="tab" aria-label="家长认证" checked="checked"/>
        <!-- 家长认证表单 -->
        <div class="tab-content bg-base-100 border-base-300 p-6 space-y-6">
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
                    v-model="parent_verification_information.id_card"
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
                <span v-if="!isLoading">提交家长认证</span>
                <span v-else>提交中...</span>
              </button>
            </div>
          </div>
        </div>
        <input type="radio" name="verification_tab" class="tab" aria-label="家教认证"/>
        <!-- 家教认证表单 -->
        <div class="tab-content bg-base-100 border-base-300 p-6 space-y-6">
          <!-- 身份证输入 -->
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
                    v-model="tutor_verification_information.id_card"
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
          </div>

          <!-- 高考成绩输入 -->
          <div class="form-control">
            <fieldset class="fieldset">
              <legend class="fieldset-legend">高考成绩</legend>
              <label class="input validator w-full">
                <svg class="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                     stroke="currentColor" stroke-width="2">
                  <path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <input
                    v-model="tutor_verification_information.college_entrance_score"
                    type="number"
                    placeholder="请输入高考成绩（0-750）"
                    required
                    min="0"
                    max="750"
                    :disabled="isLoading"
                />
              </label>
              <p class="validator-hint hidden">请输入有效的高考成绩</p>
            </fieldset>
          </div>

          <!-- 学生证上传 -->
          <div class="form-control">
            <fieldset class="fieldset">
              <legend class="fieldset-legend">学生证照片 <span class="text-red-500">*</span></legend>
              <input
                  id="student_card_input"
                  type="file"
                  accept="image/*"
                  class="file-input w-full"
                  @change="handleStudentCardSelect"
                  :disabled="isLoading"
              />
              <label class="label">请上传清晰的学生证照片（不超过1MB）</label>
            </fieldset>
          </div>

          <!-- 教师资格证上传（可选） -->
          <div class="form-control">
            <fieldset class="fieldset">
              <legend class="fieldset-legend">教师资格证照片（可选）</legend>
              <input
                  id="student_card_input"
                  type="file"
                  accept="image/*"
                  class="file-input w-full"
                  @change="handleTeacherCertificateSelect"
                  :disabled="isLoading"
              />
              <label class="label">如有教师资格证请上传（不超过1MB）</label>
            </fieldset>
          </div>

          <!-- 认证按钮 -->
          <div class="form-control mt-8">
            <button
                @click="tutor_verification"
                class="btn btn-primary"
                :class="{ 'loading': isLoading }"
                :disabled="isLoading"
            >
              <span v-if="!isLoading">提交家教认证</span>
              <span v-else>提交中...</span>
            </button>
          </div>
        </div>
      </div>


    </div>

    <!-- 模态框背景 -->
    <form method="dialog" class="modal-backdrop">
      <button :disabled="isLoading">关闭</button>
    </form>
  </dialog>
</template>

<style scoped>
/* 复用登录模态框的动画和样式 */
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.3s ease-out;
}

.input:disabled {
  @apply cursor-not-allowed opacity-50;
}

.modal-middle .modal-box {
  margin: auto;
}
</style>