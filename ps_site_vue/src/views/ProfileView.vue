<template>
  <div class="page-profile">
    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="title">
          <h1>{{ profile.username }}'s Profile</h1>
        </div>
        <ProfileCard v-bind:profile="profile" v-bind:key="profile.id" />
        <hr />
        <ExperienceCard
          v-for="job in profile.employment"
          v-bind:job="job"
          v-bind:key="job.id"
        />
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import ProfileCard from "../components/ProfileCard.vue";
import ProjectCard from "../components/ProjectCard.vue";
import EducationCard from "../components/EducationCard.vue";
import ExperienceCard from "../components/ExperienceCard.vue";
import CertificationCard from "../components/CertificationCard.vue";
import ProductCard from "../components/ProductCard.vue";

export default {
  name: "profile",
  data() {
    return {
      profile: {},
    };
  },
  components: {
    ProfileCard,
    ProjectCard,
    EducationCard,
    ExperienceCard,
    CertificationCard,
    ProductCard,
  },
  mounted() {
    this.getProfile();
  },
  watch: {
    $route(to, from) {
      if (to.name == "Profile") {
        this.getProfile();
      }
    },
  },
  methods: {
    async getProfile() {
      this.$store.commit("setIsLoading", true);
      const profile_id = this.$route.params.profile_id;
      await axios
        .get(`/api/v1/profiles/${profile_id}/`)
        .then((res) => {
          this.profile = res.data;
          document.title = this.profile.username + " | Grünluft";
        })
        .catch((err) => {
          console.log(err);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
<style>
.title {
  margin-left: 1rem;
}
</style>
