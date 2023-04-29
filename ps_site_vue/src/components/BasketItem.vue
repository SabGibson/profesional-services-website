<template>
  <tr>
    <td>
      <router-link :to="item.product.get_abs_url">{{
        item.product.name
      }}</router-link>
    </td>
    <td>£{{ item.product.price }}</td>
    <td>{{ item.quantity }}</td>
    <td>{{ getItemTotal(item).toFixed(2) }}</td>
    <td><button class="delete">delete</button></td>
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
  },
};
</script>
