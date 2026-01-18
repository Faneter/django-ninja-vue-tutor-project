<script setup>
import NavBar from "@/components/NavBar.vue";

import {onMounted, reactive, ref} from 'vue'
import request from "@/utils/request";

const isLoggedIn = ref(false)

request.post(`/user/is_logged_in`, {}).then(response => {
  isLoggedIn.value = !!response.status;
})

</script>

<template>
  <NavBar :isLoggedIn="isLoggedIn"/>
</template>
