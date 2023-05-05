<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-4by3">
        <img :src="profile.image.get_thumbnail" alt="Profile picture" />
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="title is-4">{{ profile.name }}</p>
          <p class="subtitle is-6">{{ profile.user.username }}</p>
        </div>
      </div>
      <div class="content">
        {{ profile.summary }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileCard",
  props: {
    profile: {
      type: Object,
      required: true,
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
