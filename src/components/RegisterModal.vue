<script setup>
import request from "@/utils/request";
import {reactive, ref} from "vue";

const register_information = reactive({
  phone: '',
  password: '',
  confirm_password: '',
})

const errorMessage = ref('')
const successMessage = ref('')
const isLoading = ref(false)

function register() {
  if (register_information.password === register_information.confirm_password) {
    request.post("/api/user/register", {
      phone: register_information.phone,
      password: register_information.password,
    }).then((response) => {
      console.log(response)
    })
  }
}
</script>

<template>

</template>

<style scoped>

</style>