<template>
  <swiper
    class="image-carousel"
    :slides-per-view="2"
    :space-between="1"
    @swiper="onSwiper"
    @slideChange="onSlideChange"
  >
    <swiper-slide v-for="(image, index) in images" :key="index">
      <div class="image-container" @click="openModal(index)">
        <img
          class="slider-image image"
          :src="image.image_url"
          alt="project image"
        />
      </div>
    </swiper-slide>
  </swiper>
  <div v-if="showModal" class="modal is-active">
    <div class="modal-background" @click="closeModal"></div>
    <div class="modal-content">
      <p class="image">
        <img :src="images[selectedImageIndex].image_url" alt="project image" />
      </p>
    </div>
    <button
      class="modal-close is-large"
      aria-label="close"
      @click="closeModal"
    ></button>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";

export default {
  name: "ImageCarousel",
  components: {
    Swiper,
    SwiperSlide,
  },
  props: {
    images: Object,
  },
  data() {
    return {
      showModal: false,
      selectedImageIndex: 0,
    };
  },
  methods: {
    openModal(index) {
      this.showModal = true;
      this.selectedImageIndex = index;
    },
    closeModal() {
      this.showModal = false;
    },
  },
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
<style>
.image-container {
  cursor: pointer;
}
.slider-image {
  height: 200px;
  width: 200px;
}
</style>
