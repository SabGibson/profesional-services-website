<template>
  <swiper
    class="image-carousel"
    :slides-per-view="1"
    :space-between="1"
    @swiper="onSwiper"
    @slideChange="onSlideChange"
  >
    <swiper-slide v-for="product in products">
      <CarouselProductCard v-bind:product="product" v-bind:key="product.id" />
    </swiper-slide>
  </swiper>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
import ProductCard from "./ProductCard.vue";
import CarouselProductCard from "../components/CarouselProductCard.vue";
export default {
  name: "ProductCarousel",
  components: {
    Swiper,
    SwiperSlide,
    CarouselProductCard,
  },
  props: {
    products: Object,
  },
  data() {
    return {
      showModal: false,
      selectedProductIndex: 0,
    };
  },
  methods: {},
  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log("slide change");
    };
    return {
      onSwiper,
      onSlideChange,
    };
  },
};
</script>
<style></style>
