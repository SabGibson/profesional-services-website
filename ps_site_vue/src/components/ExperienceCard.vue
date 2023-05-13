<template>
  <li class="column is-12">
    <hr class="styled-hr" />
    <div class="container">
      <div class="profile-main">
        <div class="columns is-multiline is-gapless">
          <div class="container column is-one-third">
            <h4 class="is-size-5">
              {{ job.job_title }}
            </h4>
            <p class="is-size-6 has-text-grey has-text-weight-bold">
              {{ job.company_name }} - {{ job.level }}
            </p>
            <p
              v-if="job.is_present"
              class="is-size-6 has-text-grey has-text-weight-bold"
            >
              {{ job.date_started }} to Present
            </p>
            <p v-else class="is-size-6 has-text-grey has-text-weight-bold">
              {{ job.date_started }} to {{ job.date_ended }}
            </p>
          </div>
        </div>

        <hr class="styled-hr" />

        <p class="is-size-6">{{ job.description }}</p>
      </div>
    </div>
  </li>
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
.figure-container {
  padding: 0.5rem;
}

.styled-hr {
  border-color: aqua;
}
</style>
