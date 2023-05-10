<template>
  <div class="card profile-card">
    <div class="card-image">
      <figure class="image is-4by3">
        <img :src="profile.profile.image.get_thumbnail" alt="Profile picture" />
      </figure>
    </div>
    <div class="card-content">
      <div class="profile-content">
        <div class="proflie-alias">
          <p class="title is-4">{{ user.name }}</p>
          <p class="subtitle is-6">{{ user.username }}</p>
        </div>
      </div>
      <div class="content">
        {{ user.profile.bio }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileCard",
  props: {
    user: {
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
