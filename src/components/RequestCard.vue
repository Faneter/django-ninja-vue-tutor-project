<script setup>
import request from "@/utils/request.js";
import {computed, reactive} from "vue";
import {gradeMap, paymentMap, subjectMap} from "@/utils/dictionary.js";

defineProps(['request_id'])

const request_profile = reactive({
  student_grade: '',
  subject: '',
  payment_type: '',
  salary: '',
})

const pay_text = computed(() => {
  if (request_profile.payment_type === "D") {
    return request_profile.salary + '元/日'
  } else if (request_profile.payment_type === "H") {
    return request_profile.salary + '元/小时'
  } else if (request_profile.payment_type === "C") {
    return request_profile.salary + '元 面议'
  }
})

function get_request(id) {
  request.get('order/get?id=' + id).then((response) => {
    console.log(response)
    request_profile.student_grade = gradeMap.get(response.student_grade);
    request_profile.subject = subjectMap.get(response.subject)
    request_profile.payment_type = response.payment_type;
    request_profile.salary = response.salary;
  })
}

get_request(1)

</script>

<template>
  <div class="card bg-base-100 w-64 shadow-sm">
    <div class="card-body">
      <h2 class="card-title">{{ request_profile.student_grade + request_profile.subject }}</h2>
      <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
      <div class="card-actions justify-between">
        <span class="text-xl">{{ pay_text }}</span>
        <button class="btn btn-primary">查看详情</button>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>