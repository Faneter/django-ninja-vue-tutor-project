<script setup>
import NavBar from "@/components/NavBar.vue";

import {ref} from 'vue'
import request from "@/utils/request";
import RequestModal from "@/components/order/RequestModal.vue";

const isLoggedIn = ref(false)

request.post(`/user/is_logged_in`, {}).then(response => {
  isLoggedIn.value = JSON.parse(response.status);
})

</script>

<template>
  <NavBar :isLoggedIn="isLoggedIn"/>
  <RequestModal id="request_modal"></RequestModal>
  <button class="btn" onclick="request_modal.showModal()">测试</button>
</template>
