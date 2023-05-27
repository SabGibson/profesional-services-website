import { createStore } from "vuex";

export default createStore({
  state: {
    basket: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
    loading: false,
    profile: null,
  },
  getters: {},
  mutations: {
    initStore(state) {
      if (localStorage.getItem("basket")) {
        state.basket = JSON.parse(localStorage.getItem("basket"));
      } else {
        localStorage.setItem("basket", JSON.stringify(state.basket));
      }

      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }

      if (localStorage.getItem("user_id")) {
        state.user = localStorage.getItem("user_id");
      } else {
        state.user = null;
      }
      if (localStorage.getItem("profile_id")) {
        state.profile = localStorage.getItem("profile_id");
      } else {
        state.profile = null;
      }
    },
    addToBasket(state, item) {
      const exists = state.basket.items.filter(
        (x) => x.product.id == item.product.id
      );
      if (exists.length) {
        exists[0].quantity =
          parseInt(exists[0].quantity) + parseInt(item.quantity);
      } else {
        state.basket.items.push(item);
      }

      localStorage.setItem("basket", JSON.stringify(state.basket));
    },
    setIsLoading(state, status) {
      state.loading = status;
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state, token) {
      state.token = "";
      state.isAuthenticated = false;
      state.user = null;
      state.profile = null;
    },
    clearBasket(state) {
      state.basket.items = [];

      localStorage.setItem("basket", JSON.stringify(state.basket));
    },

    setUser(state, user) {
      state.profile = user.profile.id;
      state.user = user.id;
    },
  },
  actions: {},
  modules: {},
});
