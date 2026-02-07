<script setup>
import {ref} from "vue";
import request from "@/utils/request.js";

import RequestModal from "@/components/order/RequestModal.vue";
import RequestCard from "@/components/order/RequestCard.vue";

const requests = ref([])

async function get_request_ids() {
  await request.get('/order/list/id').then(response => {
    requests.value = response;
  })
}

get_request_ids();
</script>

<template>
  <div class="container mx-auto px-4 py-4 md:px-6">
    <div class="tabs tabs-lift">
      <input type="radio" name="my_tabs_3" class="tab" aria-label="家教需求" checked="checked"/>
      <div class="tab-content bg-base-100 border-base-300 p-6">
        <RequestModal id="request_modal"></RequestModal>
        <button class="btn" onclick="request_modal.showModal()">测试</button>
        <div class="flex flex-wrap">
          <RequestCard v-for="request in requests" :request_id="request"></RequestCard>
        </div>
      </div>

      <input type="radio" name="my_tabs_3" class="tab" aria-label="教师浏览"/>
      <div class="tab-content bg-base-100 border-base-300 p-6">Tab content 2</div>

      <input type="radio" name="my_tabs_3" class="tab" aria-label="Tab 3"/>
      <div class="tab-content bg-base-100 border-base-300 p-6">Tab content 3</div>
    </div>
  </div>
</template>

<style scoped>

</style>