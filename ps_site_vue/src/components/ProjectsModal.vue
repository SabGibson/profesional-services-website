<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <form @submit.prevent="updateEducation">
        <div
          v-for="record in projects"
          v-bind:key="record.id"
          class="general-form"
        >
          <div class="field">
            <label class="label">Project Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.project_name}`"
                v-model="record.project_name"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.description}`"
                v-model="record.description"
              />
            </div>
          </div>
          <div class="image-upload">
            <input type="file" @change="uploadProjectImage($event, record)" />
          </div>
          <hr />
          <div
            class="project-image"
            v-for="image in record.images"
            v-bind:key="image.id"
          >
            <img :src="image.image_url" alt="project image" />
            <button
              type="button"
              class="button is-link is-danger"
              @click="deleteImage(record.id, image.id)"
            >
              delete
            </button>
          </div>
          <hr />
          <div class="field is-grouped">
            <div class="control">
              <button
                type="submit"
                class="button is-link"
                @click="updateProject(record)"
              >
                Update
              </button>
            </div>
            <div class="control">
              <button
                type="button"
                class="button is-link is-danger"
                @click="deleteProject(record.id)"
              >
                delete
              </button>
            </div>
          </div>
          <hr />
        </div>

        <div class="control">
          <button
            type="button"
            class="button is-link is-light"
            @click="$emit('close')"
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
    <button
      class="modal-close is-large"
      aria-label="close"
      @click="$emit('close')"
    ></button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProjectsModal",
  props: {
    projects: Object,
  },
  data() {
    return {};
  },
  methods: {
    async updateProject(record) {
      let updateForm = { ...record };
      delete updateForm.id;
      axios
        .patch(`/api/v1/profile-project/${this.record.id}/`, updateForm)
        .then((res) => {
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    },

    async uploadProjectImage(event, record) {
      const file = event.target.files[0];
      let formData = new FormData();
      formData.append("image", file);
      formData.append("project", record.id);

      axios
        .post(`/api/v1/profile-project-image/`)
        .then((res) => {
          this.$emit("uploaded-image");
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async deleteImage(id) {
      axios
        .delete(`/api/v1/profile-project-image/${id}/`)
        .then(() => {
          this.$emit("deleted");
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async deleteProject(id) {
      axios
        .delete(`/api/v1/profile-project/${id}/`)
        .then(() => {
          this.$emit("deleted");
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
