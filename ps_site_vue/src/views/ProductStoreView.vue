<template>
  <section>
    <div class="columns is-multiline">
      <div
        v-for="product in paginatedProducts"
        :key="product.id"
        class="column is-one-quarter"
      >
        <StoreProductCard v-bind:product="product"></StoreProductCard>
      </div>
    </div>

    <!-- Pagination -->
    <nav class="pagination" role="navigation" aria-label="pagination">
      <button
        class="pagination-previous"
        :disabled="currentPage <= 1"
        @click="currentPage--"
      >
        Previous
      </button>
      <button
        class="pagination-next"
        :disabled="currentPage >= numPages"
        @click="currentPage++"
      >
        Next
      </button>
      <ul class="pagination-list">
        <li v-for="n in numPages" :key="n">
          <a
            class="pagination-link"
            :class="{ 'is-current': n === currentPage }"
            @click="currentPage = n"
            >{{ n }}</a
          >
        </li>
      </ul>
    </nav>
  </section>
</template>

<script>
import StoreProductCard from "../components/StoreProductCard.vue";
import axios from "axios";
export default {
  name: "ProductStore",
  components: {
    StoreProductCard,
  },
  data() {
    return {
      products: [],
      currentPage: 1,
      itemsPerPage: 20,
    };
  },
  computed: {
    paginatedProducts() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.products.slice(start, start + this.itemsPerPage);
    },
    numPages() {
      return Math.ceil(this.products.length / this.itemsPerPage);
    },
  },
  methods: {
    async fetchProducts() {
      axios
        .get("api/v1/products/list/")
        .then((res) => {
          this.products = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.fetchProducts();
  },
};
</script>
