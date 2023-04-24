import { createStore } from "vuex";

export default createStore({
  state: {
    basket: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
    loading: false,
  },
  getters: {},
  mutations: {
    initStore(state) {
      if (localStorage.getItem("basket")) {
        state.basket = JSON.parse(localStorage.getItem("basket"));
      } else {
        localStorage.setItem("basket", JSON.stringify(state.basket));
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
  },
  actions: {},
  modules: {},
});
