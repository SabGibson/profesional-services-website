<template>
  <div class="page-profile">
    <div class="columns is-multiline">
      <div class="column is-8">
        <div class="title">
          <h1>{{ profile.username }}'s Profile</h1>
        </div>
        <div class="">
          <ProfileCard v-bind:profile="profile" v-bind:key="profile.id" />
        </div>

        <hr />

        <ul class="column is-12 box">
          <div class="columns is-multiline">
            <h4 class="title has-size-4 column is-10">Experience</h4>
            <i @click="editExperience" class="column is-1 far fa-edit"></i>
          </div>

          <ExperienceCard
            v-for="job in profile.employment"
            v-bind:job="job"
            v-bind:key="job.id"
          />
          <ExperienceModal
            v-if="showModal.experience"
            v-bind:experience="profile.employment"
            @close="showModal.experience = false"
          />
        </ul>
        <ul class="column is-12 box">
          <div class="columns is-multiline">
            <h4 class="title has-size-4 column is-10">Education</h4>
            <i @click="editEducation" class="column is-1 far fa-edit"></i>
          </div>
          <EducationCard
            v-for="education in profile.education"
            v-bind:education="education"
            v-bind:key="education.id"
          />
          <EducationModal
            v-if="showModal.education"
            v-bind:education="profile.education"
            @close="showModal.education = false"
            @deleted="confirmEduDelete"
          />
        </ul>
        <ul class="column is-12 box">
          <div class="columns is-multiline">
            <h4 class="title has-size-4 column is-10">Skills</h4>
            <i @click="editSkills" class="column is-1 far fa-edit"></i>
          </div>
          <SkillsCard
            v-for="skill in profile.skills"
            v-bind:skills="skill"
            v-bind:key="skill.id"
          />
          <SkillsModalVue
            v-if="showModal.skills"
            v-bind:skills="profile.skills"
            @close="showModal.skills = false"
            @deleted="confirmSklDelete"
          />
        </ul>
        <ul class="column is-12 box">
          <div class="columns is-multiline">
            <h4 class="title has-size-4 column is-10">
              Certifications & Licences
            </h4>
            <i @click="editCertification" class="column is-1 far fa-edit"></i>
          </div>
          <CertificationCard
            v-for="cert in profile.certifications"
            v-bind:skills="cert"
            v-bind:key="cert.id"
          />
          <CertificationsModal
            v-if="showModal.certifications"
            v-bind:certifications="profile.certifications"
            @close="showModal.certifications = false"
          />
        </ul>
      </div>
      <div class="column is-4 side-bar">
        <ul class="column is-12 box">
          <div class="columns is-multiline">
            <h4 class="title has-size-4 column is-10">
              Projects by {{ profile.first_name }}
            </h4>
            <i @click="editProjects" class="column is-1 far fa-edit"></i>
          </div>
          <hr />
          <ProjectCard
            v-for="project in profile.projects"
            v-bind:project="project"
            v-bind:key="project.id"
          />
          <ProjectsModal
            v-if="showModal.projects"
            v-bind:projects="profile.projects"
            @close="showModal.projects = false"
          />
        </ul>
        <ul class="column is-12 box">
          <h4 class="title has-size-4">Products by {{ profile.first_name }}</h4>
          <ProductCarousel
            v-if="products.length > 0"
            v-bind:products="products"
          />
          <button
            v-else
            class="is-dark button is-center load-button"
            @click="getProducts"
          >
            show products
          </button>
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
import ProductCarousel from "../components/ProductCarousel.vue";
import EducationModal from "../components/EducationModal.vue";
import ExperienceModal from "@/components/ExperienceModal.vue";
import CertificationsModal from "@/components/CertificationsModal.vue";
import SkillsModalVue from "@/components/SkillsModal.vue";
import ProjectsModal from "@/components/ProjectsModal.vue";
import { toast } from "bulma-toast";

export default {
  name: "profile",
  data() {
    return {
      profile: {},
      products: {},
      showModal: {
        education: false,
        experience: false,
        skills: false,
        certifications: false,
        projects: false,
      },
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
    ProductCarousel,
    ExperienceModal,
    EducationModal,
    CertificationsModal,
    SkillsModalVue,
    ProjectsModal,
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
    confirmSklDelete() {
      this.showModal.skills = false;
      toast({
        message: `A skill entry was deleted.`,
        type: "is-info",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
    confirmEduDelete() {
      this.showModal.education = false;
      toast({
        message: `An education entry was deleted.`,
        type: "is-info",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
    editProjects() {
      console.log(this.profile);
      this.showModal.projects = true;
    },
    editCertification() {
      console.log(this.profile.certifications);
      this.showModal.certifications = true;
    },
    editSkills() {
      console.log(this.profile.skills);
      this.showModal.skills = true;
    },
    editEducation() {
      this.showModal.education = true;
    },
    editExperience() {
      console.log(this.profile.employment);
      this.showModal.experience = true;
    },

    deleteExperience() {
      axios
        .delete(`/api/v1/profile-employment/${this.job.id}/`) // replace with your actual API endpoint
        .then(() => {
          this.$emit("deleted");
        })
        .catch((err) => {
          console.error(err);
        });
    },

    async getProducts() {
      this.$store.commit("isLoading", true);

      await axios
        .post("/api/v1/products/search/", { query: this.profile.username })
        .then((res) => {
          this.products = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
      this.$store.commit("isLoading", false);
    },
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
.load-button {
  margin-left: 1rem;
}
</style>
products/search/
