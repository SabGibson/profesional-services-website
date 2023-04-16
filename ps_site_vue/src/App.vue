<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"
          ><strong>Grünluft</strong></router-link
        >
        <a
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          class="navbar-burger"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link to="/store" class="navbar-item">Store</router-link>
          <router-link to="/gallery" class="navbar-item">Gallery</router-link>
          <router-link to="/profile" class="navbar-item">Profile</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light"
                >Login</router-link
              >
              <router-link to="/basket" class="button is-success">
                <span class="icon">
                  <i class="fa fa-shopping-cart"></i>
                </span>
                <span>Basket ({{ basketTotalSize }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-right">Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      basket: {
        items: [],
      },
    };
  },
  beforeCreate() {
    this.$store.commit("initStore");
  },
  mounted() {
    this.basket = this.$store.state.basket;
  },
  computed: {
    basketTotalSize() {
      let totalLenght = 0;

      for (let i = 0; i < this.basket.items.length; i++) {
        totalLenght += this.basket.items[i].quantity;
      }

      return totalLenght;
    },
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>
