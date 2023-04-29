<template>
  <div class="page-basket">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Basket</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="basketTotalLength">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <BasketItem
              v-for="item in basket.items"
              v-bind:key="item.product.id"
              v-bind:initialItem="item"
            />
          </tbody>
        </table>
        <div class="column is-full" v-else>
          <strong
            ><h3 class="subtitle is-4 has-text-start">
              Your Grünluft Basket is empty
            </h3>
          </strong>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BasketItem from "@/components/BasketItem.vue";
export default {
  name: "Basket",
  data() {
    return {
      basket: {
        items: [],
      },
    };
  },
  components: { BasketItem },
  mounted() {
    document.title = "Basket" + " | Grünluft";
    this.basket = this.$store.state.basket;
    this.getBasket();
  },
  computed: {
    basketTotalLength() {
      return this.basket.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
  },

  methods: {
    async getBasket() {},
  },
};
</script>
