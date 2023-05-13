<template>
  <div class="column is-8">
    <div class="box">
      <div class="profile-main">
        <div class="columns is-multiline is-gapless">
          <div class="container column is-one-third">
            <h2 class="is-size-4 has-text-weight-bold">
              {{ profile.full_name }}
            </h2>
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
  name: "ExperienceCard",
  props: {
    job: Object,
  },
};
</script>

<style>
.image {
  border: 3px solid grey;
  border-radius: 50%;
}

.profile-main {
  margin-left: 1.5rem;
  margin-right: 1.5rem;
  margin-top: 0.5rem;
}

.box {
  background-color: #caccce;
}

.figure-container {
  padding: 0.5rem;
}

.styled-hr {
  border-color: aqua;
}
</style>
