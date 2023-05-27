<template>
  <div class="column is-12">
    <div class="box">
      <figure class="image is-5by4 mb-4">
        <img :src="product.get_thumbnail" alt="product image" />
      </figure>
      <h3 class="is-size-6">{{ product.name }}</h3>
      <p class="is-size-7 has-text-grey">£{{ product.price }}</p>
      <router-link
        :to="`/profiles/${product.profile}/`"
        class="is-text no-padding-left column"
        ><p>by: {{ product.creator }}</p></router-link
      >
      <router-link
        v-bind:to="product.get_abs_url"
        class="button is-success column"
        >View details</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "StoreProductCard",
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
.no-padding-left {
  padding-left: 0 !important;
}
</style>
