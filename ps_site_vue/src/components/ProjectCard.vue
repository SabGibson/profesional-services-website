<template>
  <div class="card cert-card">
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="title is-4">{{ project.project_name }}</p>
        </div>
      </div>
      <div class="content">
        <p>{{ project.description }}</p>
      </div>
      <div class="image-carousel">
        <carousel>
          <slide v-for="image in project.images" v-bind:key="image.id">
            <img src="image.get_image" alt="Project Image" />
          </slide>
        </carousel>
      </div>
    </div>
  </div>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";
export default {
  name: "ProjectCard",

  components: {
    Carousel,
    Slide,
  },
  props: {
    project: {
      type: Object,
    },
  },
};
</script>

<style>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
