<template>
  <div class="card profile-card">
    <div class="card-content">
      <div class="profile-content">
        <div class="proflie-alias">
          <p class="title is-4">{{ education.qualification_name }}</p>
          <p class="subtitle is-6">{{ education.institution_name }}</p>
        </div>
      </div>
      <div class="content">
        {{ education.description }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EducationCard",
  props: {
    education: {
      type: Object,
    },
  },
};
</script>
