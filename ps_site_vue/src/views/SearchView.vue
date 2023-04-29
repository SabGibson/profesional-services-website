<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-grey">Searched for: "{{ query }}"</h2>
      </div>
      <ProductCard
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ProductCard from "@/components/ProductCard.vue";

export default {
  name: "Search",
  data() {
    return {
      products: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search" + " | Grünluft";
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");
      this.executeSearch();
    }
  },
  components: { ProductCard },
  methods: {
    async executeSearch() {
      this.$store.commit("isLoading", true);

      await axios
        .post("/api/v1/products/search/", { query: this.query })
        .then((res) => {
          this.products = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
      this.$store.commit("isLoading", false);
    },
  },
};
</script>
