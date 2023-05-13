<template>
  <li class="column is-12">
    <hr class="styled-hr" />
    <div class="container">
      <div class="profile-main">
        <p class="is-size-5 has-text-grey">
          {{ skills.skill_name }}
        </p>
        <p class="is-size-6 has-text-grey">{{ skills.description }}</p>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  name: "SkillsCard",
  props: {
    skills: Object,
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
