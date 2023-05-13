<template>
  <div class="cert-card">
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="title is-4">{{ project.project_name }}</p>
        </div>
      </div>
      <div class="content">
        <p>{{ project.description }}</p>
      </div>
      <hr />
      <div class="container">
        <ImageCarousel v-bind:images="project.images" />
      </div>
    </div>
  </div>
</template>

<script>
import ImageCarousel from "../components/ImageCarousel.vue";
export default {
  name: "ProjectCard",

  components: {
    ImageCarousel,
  },
  props: {
    project: {
      type: Object,
    },
  },
};
</script>
