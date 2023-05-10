<template>
  <div class="card profile-card">
    <div class="card-content">
      <div class="profile-content">
        <div class="proflie-alias">
          <p class="title is-4">{{ job.job_title }}</p>
          <p class="subtitle is-6">{{ job.company_name }}</p>
        </div>
      </div>
      <div class="content">
        {{ job.description }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ExperienceCard",
  props: {
    job: {
      type: Object,
    },
  },
};
</script>
