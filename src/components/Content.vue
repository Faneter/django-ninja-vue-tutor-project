<script setup>
import {reactive, ref} from "vue";
import request from "@/utils/request.js";

import RequestModal from "@/components/order/RequestModal.vue";
import RequestCard from "@/components/order/RequestCard.vue";
import Paginator from "@/widget/Paginator.vue";

const requests = reactive({
  content: null,
  page_num: null,
})

request.get('/order/list/page').then((response) => {
  requests.page_num = response
})

async function get_request_ids(page = 1) {
  await request.get(`/order/list/id?page=${page}`).then(response => {
    requests.content = response;
  })
}

const page_handler = (page) => {
  get_request_ids(page);
}

get_request_ids(2);
</script>

<template>
  <div class="container mx-auto px-4 py-4 md:px-6">
    <div class="tabs tabs-lift">
      <input type="radio" name="my_tabs_3" class="tab" aria-label="家教需求" checked="checked"/>
      <div class="tab-content bg-base-100 border-base-300 p-6">
        <RequestModal id="request_modal"></RequestModal>
        <button class="btn" onclick="request_modal.showModal()">测试</button>
        <div class="flex flex-wrap">
          <RequestCard v-for="request in requests.content" :request_id="request"></RequestCard>
          <Paginator :page_num="requests.page_num" :handler="page_handler"></Paginator>
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