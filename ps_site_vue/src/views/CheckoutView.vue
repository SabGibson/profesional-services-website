<template>
  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title has-text-start">Checkout</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in basket.items" v-bind:key="item.product.id">
              <td>{{ item.product.name }}</td>
              <td>£{{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>£{{ getItemtotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="2">Total</td>
              <td>{{ basketTotalLength }}</td>
              <td>{{ basketTotalPrice.toFixed(2) }}</td>
            </tr>
          </tfoot>
        </table>
      </div>
      <div class="column is-12 box">
        <h2 class="subtitle">Order Details</h2>
        <p class="has-text-grey mb-4">*Required fields</p>
        <div class="columns is-multili">
          <div class="column is-6">
            <div class="field">
              <label>First name*</label>
              <div class="contorl">
                <input type="text" class="input" v-model="first_name" />
              </div>
            </div>
            <div class="field">
              <label>Last name*</label>
              <div class="contorl">
                <input type="text" class="input" v-model="last_name" />
              </div>
            </div>
            <div class="field">
              <label>Email*</label>
              <div class="contorl">
                <input type="email" class="input" v-model="email" />
              </div>
              <div class="field">
                <label>Phone</label>
                <div class="contorl">
                  <input type="tel" class="input" v-model="tel" />
                </div>
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="field">
              <label>Address*</label>
              <div class="contorl">
                <input type="text" class="input" v-model="address" />
              </div>
            </div>
            <div class="field">
              <label>Postal code*</label>
              <div class="contorl">
                <input type="text" class="input" v-model="post_code" />
              </div>
            </div>
            <div class="field">
              <label>Country*</label>
              <div class="contorl">
                <input type="text" class="input" v-model="country" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-12">
        <div class="notification is-danger mt-4" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <hr />

        <div class="mb-5" id="card-element"></div>
        <template v-if="basketTotalLength">
          <hr />

          <button class="button is-dark" @click="submitForm">
            Proceed to payment
          </button>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Checkout",
  data() {
    return {
      basket: {
        items: [],
      },
      stripe: {},
      first_name: "",
      last_name: "",
      email: "",
      tel: "",
      address: "",
      post_code: "",
      country: "",
      errors: [],
    };
  },
  mounted() {
    document.title = document.title = "Checkout" + " | Grünluft";
    this.basket = this.$store.state.basket;
  },
  methods: {
    getItemtotal(item) {
      return item.quantity * item.product.price;
    },
  },
  computed: {
    basketTotalLength() {
      return this.basket.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },

    basketTotalPrice() {
      return this.basket.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity * curVal.product.price);
      }, 0);
    },
  },
};
</script>
