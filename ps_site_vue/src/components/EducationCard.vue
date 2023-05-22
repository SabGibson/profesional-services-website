<template>
  <li class="column is-12">
    <hr class="styled-hr" />
    <div class="container">
      <div class="profile-main">
        <div class="columns is-multiline is-gapless">
          <div class="container column is-two-thirds">
            <h4 class="is-size-5">
              {{ education.institution_name }}
            </h4>
            <p class="is-size-6 has-text-grey has-text-weight-bold">
              {{ education.qualification_name }} - {{ education.level }}
            </p>
            <p class="is-size-6 has-text-grey has-text-weight-bold">
              {{ education.date_achieved }}
            </p>
          </div>
        </div>

        <hr class="styled-hr" />

        <p class="is-size-6">{{ education.description }}</p>
      </div>
    </div>
  </li>
</template>

<style>
.button-container {
  display: flex;
  justify-content: flex-start;
  align-items: flex-end;
}
</style>

<script>
import axios from "axios";
export default {
  name: "EducationCard",
  props: {
    education: Object,
  },
  methods: {},
};
</script>

<style>
.figure-container {
  padding: 0.5rem;
}
</style>
