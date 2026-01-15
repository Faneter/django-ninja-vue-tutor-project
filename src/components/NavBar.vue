<script setup>
import LoginModal from "@/components/LoginModal.vue";
import request from "@/utils/request.js";

const props = defineProps(['isLoggedIn'])

function logout() {
  request.post(`/user/logout`, {}).finally(() => {
    location.reload()
  })
}
</script>

<template>
  <LoginModal/>
  <div class="navbar bg-base-100 mb-40 shadow-sm">
    <div class="navbar-start">
      <button class="btn btn-ghost text-xl">daisyUI</button>
    </div>
    <div v-if="isLoggedIn === true" class="navbar-end">
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
          <div class="indicator">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                 stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            <span class="badge badge-sm indicator-item">8</span></div>
        </div>
        <div tabindex="0" class="mt-3 z-1 card card-compact w-52 dropdown-content bg-base-100 shadow">
          <div class="card-body"><span class="font-bold text-lg">8 件商品</span> <span
              class="text-info">小计: $999</span>
            <div class="card-actions">
              <button class="btn btn-primary btn-block">查看购物车</button>
            </div>
          </div>
        </div>
      </div>
      &nbsp;&nbsp;
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS Navbar component"
                 src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp">
          </div>
        </div>
        <ul tabindex="0" class="mt-3 z-1 p-2 shadow menu menu-sm dropdown-content bg-base-100 rounded-box w-52">
          <li>
            <button class="justify-between">个人资料 <span class="badge">新</span></button>
          </li>
          <li>
            <button>设置</button>
          </li>
          <li>
            <button @click="logout">登出</button>
          </li>
        </ul>
      </div>
      &nbsp;&nbsp;
    </div>
    <div v-else class="navbar-end">
      <button class="btn" onclick="login_modal.showModal()">登录</button>
      &nbsp;&nbsp;
      <button class="btn">注册</button>
      &nbsp;&nbsp;
    </div>
  </div>
</template>

<style scoped>
@import "@/assets/main.css";
</style>