<script setup>
defineProps(['successMessage', 'errorMessage', 'isLoading']);
</script>

<template>
  <dialog :id="$attrs.id" class="modal modal-middle">
    <div class="modal-box max-w-md p-8">
      <!-- 关闭按钮 -->
      <form method="dialog" class="absolute right-4 top-4">
        <button class="btn btn-sm btn-circle btn-ghost">✕</button>
      </form>

      <!-- 标题 -->
      <h3 class="text-2xl font-bold text-center mb-8">用户登录</h3>

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
      <div class="space-y-6">
        <slot></slot>
      </div>
    </div>

    <!-- 模态框背景 -->
    <form method="dialog" class="modal-backdrop">
      <button :disabled="isLoading">关闭</button>
    </form>
  </dialog>
</template>

<style scoped>
/* 添加淡入动画 */
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

/* 确保输入框在加载时样式一致 */
.input:disabled {
  @apply cursor-not-allowed opacity-50;
}

/* 模态框居中优化 */
.modal-middle .modal-box {
  margin: auto;
}
</style>