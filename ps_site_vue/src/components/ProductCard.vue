<template>
  <div class="column is-3">
    <div class="box">
      <figure class="image mb-4">
        <img :src="product.get_thumbnail" />
      </figure>
      <h3 class="is-size-4">{{ product.name }}</h3>
      <p class="is-size-6 has-text-grey">£{{ product.price }}</p>
      <router-link v-bind:to="product.get_abs_url" class="button is-dark mt-4"
        >View details</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductCard",
  props: {
    product: Object,
  },
};
</script>

<style>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
