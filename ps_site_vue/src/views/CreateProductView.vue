<template>
  <div class="container">
    <h1 class="title">Create a New Product</h1>
    <form @submit.prevent="onSubmit">
      <div class="field">
        <label class="label" for="name">Product Name</label>
        <div class="control">
          <input class="input" type="text" id="name" v-model="product.name" />
        </div>
      </div>
      <div class="field">
        <label class="label" for="description">Description</label>
        <div class="control">
          <textarea
            class="textarea"
            id="description"
            v-model="product.description"
          ></textarea>
        </div>
      </div>
      <div class="field">
        <label class="label" for="price">Price</label>
        <div class="control">
          <input
            class="input"
            type="number"
            id="price"
            step="0.01"
            v-model="product.price"
          />
        </div>
      </div>
      <div class="field">
        <label class="label" for="category">Category</label>
        <div class="control">
          <div class="select is-fullwidth">
            <select v-model="product.category">
              <option
                v-for="category in categories"
                :key="category.id"
                :value="category.id"
              >
                {{ category.name }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="field">
        <label class="label" for="image">Image</label>
        <div class="control">
          <input
            class="input"
            type="file"
            id="image"
            ref="file"
            v-on:change="handleFileUpload()"
          />
        </div>
      </div>
      <div class="field">
        <div class="control">
          <button class="button is-success is-link" type="submit">
            Submit
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      product: {
        name: "",
        description: "",
        price: "",
        slug: "",
        category: null,
        image: null,
      },
      categories: [],
    };
  },
  methods: {
    fetchCategories() {
      axios.get("/api/v1/categories/").then((res) => {
        this.categories = res.data;
      });
    },
    handleFileUpload() {
      this.product.image = this.$refs.file.files[0];
    },
    onSubmit() {
      let formData = new FormData();
      formData.append("name", this.product.name);
      formData.append("description", this.product.description);
      formData.append("price", this.product.price);
      formData.append("category", this.product.category);
      formData.append("image", this.product.image);

      axios
        .post("/api/v1/product-admin/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(() => this.$router.push(`/`))
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.fetchCategories();
  },
};
</script>
