<script setup>
import NavBar from "@/components/NavBar.vue";

import {ref} from 'vue'
import request from "@/utils/request";
import Content from "@/components/Content.vue";

const isLoggedIn = ref(false)

request.post(`/user/is_logged_in`, {}).then(response => {
  isLoggedIn.value = JSON.parse(response.status);
})

</script>

<template>
  <NavBar :isLoggedIn="isLoggedIn"/>
  <Content></Content>
</template>
