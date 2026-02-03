<script setup>
import RequestModal from "@/components/order/RequestModal.vue";
import RequestCard from "@/components/RequestCard.vue";
</script>

<template>
  <div class="container mx-auto px-4 md:px-6">
    <div class="tabs tabs-lift">
      <input type="radio" name="my_tabs_3" class="tab" aria-label="家教需求" checked="checked"/>
      <div class="tab-content bg-base-100 border-base-300 p-6">
        <RequestModal id="request_modal"></RequestModal>
        <button class="btn" onclick="request_modal.showModal()">测试</button>
        <RequestCard></RequestCard>
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