<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>Grünluft</strong> <span><i class="fa fa-wind"></i></span
        ></router-link>
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
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input
                    type="text"
                    class="input"
                    name="query"
                    placeholder="Search for a product"
                  />
                </div>
                <div class="control">
                  <button class="button is-success">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end">
          <router-link to="/" class="navbar-item">Home</router-link>
          <router-link to="/store" class="navbar-item">Store</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <button
                to="/"
                class="button is-dark"
                v-if="$store.state.isAuthenticated"
                @click="toProfile"
              >
                My Profile
              </button>
              <button
                to="/"
                class="button is-dark"
                v-if="$store.state.isAuthenticated"
                @click="logout"
              >
                Logout
              </button>
              <router-link
                v-if="$store.state.isAuthenticated"
                to="/create/new-product"
                class="button is-light"
                >Create Product</router-link
              >
              <router-link to="/log-in" class="button is-light" v-else
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

    <div
      class="is-loading-bar has-text-centered"
      v-bind:class="{ 'is-loading': $store.state.loading }"
    >
      <div class="lds-dual-ring"></div>
    </div>
    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-right">Copyright (c) 2023</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

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
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.basket = this.$store.state.basket;
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("user_id");
      localStorage.removeItem("profile_id");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
    toProfile() {
      this.$router.push(`/profiles/${this.$store.state.profile}`);
    },
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
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: "";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 5px solid pink;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1, 2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
