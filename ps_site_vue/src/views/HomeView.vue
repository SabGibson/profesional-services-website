<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Grünluft</p>
        <p class="subtitle">
          The best site for portfolios and direct buy professional services
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <ProductCard
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductCard from "../components/ProductCard";

export default {
  name: "HomeView",

  data() {
    return {
      latestProducts: [],
    };
  },

  components: { ProductCard },
  mounted() {
    document.title = "Home" + " | Grünluft";
    this.getLatestProducts();
  },

  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/latest-products/")
        .then((res) => {
          this.latestProducts = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
