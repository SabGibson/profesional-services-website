<template>
  <div class="page-profile">
    <div class="columns is-multiline">
      <div class="column is-7">
        <div class="title">
          <h1>{{ profile.username }}'s Profile</h1>
        </div>
        <ProfileCard v-bind:profile="profile" v-bind:key="profile.id" />
        <hr />
        <ul class="column is-12 box">
          <h4 class="title has-size-4">Experience</h4>
          <ExperienceCard
            v-for="job in profile.employment"
            v-bind:job="job"
            v-bind:key="job.id"
          />
        </ul>
        <ul class="column is-12 box">
          <h4 class="title has-size-4">Education</h4>
          <EducationCard
            v-for="education in profile.education"
            v-bind:education="education"
            v-bind:key="education.id"
          />
        </ul>
        <ul class="column is-12 box">
          <h4 class="title has-size-4">Skills</h4>
          <SkillsCard
            v-for="skill in profile.skills"
            v-bind:skills="skill"
            v-bind:key="skill.id"
          />
        </ul>
        <ul class="column is-12 box">
          <h4 class="title has-size-4">Certifications & Licences</h4>
          <CertificationCard
            v-for="cert in profile.certifications"
            v-bind:skills="cert"
            v-bind:key="cert.id"
          />
        </ul>
      </div>
      <div class="column is-5 side-bar">
        <ul class="column is-12 box">
          <h4 class="title has-size-4">Projects by {{ profile.first_name }}</h4>
          <ProjectCard
            v-for="project in profile.projects"
            v-bind:project="project"
            v-bind:key="project.id"
          />
        </ul>
        <ul class="column is-12 box">
          <h4 class="title has-size-4">Products by {{ profile.first_name }}</h4>
          <CertificationCard
            v-for="skill in profile.certifications"
            v-bind:skills="skill"
            v-bind:key="skill.id"
          />
        </ul>
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
import SkillsCard from "../components/SkillsCard.vue";

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
    SkillsCard,
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
.side-bar {
  margin-top: 5rem;
}
/* .box {
  background-color: #99d98c;
} */
</style>
