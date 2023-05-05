<template>
  <div class="page-profile"></div>
</template>
<script>
export default {
  name: "profile",
  data() {
    return {
      token: "",
      user: {},
    };
  },
  mounted() {
    document.title = document.title = `${user.username}` + " | Grünluft";
  },
};
</script>
