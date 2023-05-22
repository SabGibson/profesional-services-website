<template>
  <div class="column is-12">
    <div class="box">
      <div class="profile-main">
        <div class="columns is-multiline is-gapless">
          <figure class="figure-container column is-11">
            <img
              class="profile image is-rounded is-128x128"
              :src="profile.get_thumbnail"
            />
          </figure>
          <div class="column is-1">
            <span class="icon">
              <i @click="openEditModal" class="far fa-edit"></i>
            </span>
          </div>
          <div class="container column is-one-third">
            <h3 class="is-size-4 has-text-weight-bold">
              {{ profile.full_name }}
            </h3>
            <p class="is-size-6 has-text-grey has-text-weight-bold">
              @{{ profile.username }}
            </p>
          </div>
        </div>

        <hr class="styled-hr" />

        <p class="is-size-6">{{ profile.bio }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileCard",
  props: {
    profile: Object,
  },
  methods: {
    openEditModal() {
      console.log("profile edit clicked");
    },
  },
};
</script>

<style>
.profile.image {
  border: 3px solid #000;
  border-radius: 50%;
  background-color: #fff;
}

.profile-main {
  margin-left: 1.5rem;
  margin-right: 1.5rem;
  margin-top: 0.5rem;
}

.figure-container {
  padding: 0.5rem;
}

.styled-hr {
  border-color: aqua;
}
</style>
