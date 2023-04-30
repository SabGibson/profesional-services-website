import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Product from "../views/ProductView.vue";
import Category from "../views/Categoryview.vue";
import Search from "../views/SearchView.vue";
import Basket from "../views/BasketView.vue";
import Signup from "../views/SignupView.vue";
import Login from "../views/LoginView.vue";
import Account from "../views/AccountView.vue";
import Checkout from "../views/CheckoutView.vue";
import store from "../store";
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/search",
    name: "search",
    component: Search,
  },
  {
    path: "/basket",
    name: "basket",
    component: Basket,
  },
  {
    path: "/sign-up",
    name: "sign-up",
    component: Signup,
  },
  {
    path: "/log-in",
    name: "log-in",
    component: Login,
  },
  {
    path: "/account",
    name: "Account",
    component: Account,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/basket/checkout",
    name: "checkout",
    component: Checkout,
    // meta: {
    //   requireLogin: true,
    // },
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/:category_slug/:product_slug/",
    name: "product",
    component: Product,
  },
  {
    path: "/:category_slug/",
    name: "category",
    component: Category,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthrnticated
  ) {
    next({ name: "log-in", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
