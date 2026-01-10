<script setup>
import {onMounted, reactive, ref} from 'vue'
import request from "@/utils/request";

const user_information = reactive(
    {
      phone: '',
      password: '',
    }
)

const _test_auth = ref('')

function login() {
  request.post(`/user/login`, {
    phone: user_information.phone,
    password: user_information.password,
  }).then(data => {
    console.log(data)
  })
}

function logout() {
  request.post(`/user/logout`, {})
}

function test() {
  request.get('/user/test').then(data => {
    console.log(data)
  })
}

function test_auth() {
  request.get('/user/test_auth').then(data => {
    test_auth.value = data
  }).catch(function (error) {
    test_auth.value = error
  });
}

onMounted(() => {
  request.get(`/hello`).then(data => {
    console.log(data)
  })
})

</script>

<template>
  <input type="text" v-model="user_information.phone"/>
  <input type="text" v-model="user_information.password"/>
  <button class="btn" @click="login">Login</button>
  <button @click="logout">Logout</button>
  <span>{{ _test_auth }}</span>
  <button @click="test_auth">Test Auth</button>
  <button @click="test">Test</button>
</template>
