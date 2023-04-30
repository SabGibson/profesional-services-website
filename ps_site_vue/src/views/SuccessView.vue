<template>
  <div class="page-success">
    <div class="columns multiline">
      <div class="column is-12">
        <h1 class="title">Order Complete</h1>
      </div>

      <p>Your order has been revieved and will be processed within 24 hours</p>
    </div>
  </div>
</template>
<script>
export default {
  name: "Success",
  mounted() {
    document.title = document.title = "Success" + " | Grünluft";
  },
};
</script>
