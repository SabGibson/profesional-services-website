<template>
  <tr>
    <td>
      <router-link :to="item.product.get_abs_url">{{
        item.product.name
      }}</router-link>
    </td>
    <td>£{{ item.product.price }}</td>
    <td>
      <a @click="decrementQuantity(item)">-</a>
      {{ item.quantity }}
      <a @click="incrementQuantity(item)">+</a>
    </td>
    <td>{{ getItemTotal(item).toFixed(2) }}</td>
    <td>
      <button class="delete" @click="removeFromBasket(item)">delete</button>
    </td>
  </tr>
</template>
<script>
export default {
  name: "BasketItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    decrementQuantity(item) {
      item.quantity -= 1;
      if (item.quantity === 0) {
        this.$emit("removeFromBasket", item);
      }
      this.updateBasket();
    },
    incrementQuantity(item) {
      item.quantity += 1;
      this.updateBasket();
    },
    updateBasket() {
      localStorage.setItem("basket", JSON.stringify(this.$store.state.basket));
    },
  },
  removeFromBasket(item) {
    this.$emit("removeFromBasket", item);
    this.updateBasket();
  },
};
</script>
