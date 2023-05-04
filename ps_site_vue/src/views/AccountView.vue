<template>
  <div class="page-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="title">
          <h1 class="title">Account</h1>
        </div>

        <div class="column is-12">
          <h2 class="subtitle">My Orders</h2>

          <OrderSummary
            v-for="order in orders"
            v-bind:key="order.id"
            v-bind:order="order"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import OrderSummary from "@/components/OrderSummary.vue";

export default {
  name: "Account",
  data() {
    return {
      account: {},
      orders: [],
    };
  },
  mounted() {
    document.title = document.title = "My Account" + " | Grünluft";
    this.getMyOrders();
  },
  methods: {
    async getMyOrders() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/orders/")
        .then((res) => {
          this.orders = res.data;
        })
        .catch((err) => {
          console.log(err);
        });

      this.$store.commit("setIsLoading", false);
    },
  },

  components: {
    OrderSummary,
  },
};
</script>
