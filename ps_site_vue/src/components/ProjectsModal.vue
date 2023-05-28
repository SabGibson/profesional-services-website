<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <div class="control">
        <button
          type="button"
          class="button is-link is-success"
          @click="newProjectRecord"
        >
          New Record
        </button>
        <h2>Edit Projects</h2>
        <div class="new-record-form" v-if="showModal">
          <form @submit.prevent="createNewRecord">
            <div class="field">
              <label class="label">Project name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.project_name"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Description</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.description"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Images</label>
              <div class="control">
                <input type="file" @change="onFileChange" multiple />
              </div>
            </div>
            <div class="field is-grouped">
              <div class="control">
                <button type="submit" class="button is-link">Save</button>
              </div>
              <div class="control">
                <button
                  type="button"
                  class="button is-link is-light"
                  @click="showModal = false"
                >
                  Cancel
                </button>
              </div>
            </div>
          </form>
          <hr />
        </div>
      </div>
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
              @click="deleteImage(image.id)"
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
    return {
      showModal: false,
      newRecord: {
        project_name: "",
        description: "",
      },
    };
  },
  methods: {
    newProjectRecord() {
      this.showModal = true;
      this.newRecord = {
        project_name: "",
        description: "",
        images: "",
      };
    },
    onFileChange(event) {
      this.newRecord.images = event.target.files;
    },
    async createNewRecord() {
      let formData = new FormData();
      formData.append("project_name", this.newRecord.project_name);
      formData.append("description", this.newRecord.description);

      axios
        .post("/api/v1/profile-project/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(async (res) => {
          this.newRecord = {
            project_name: "",
            description: "",
            images: "",
          };

          const projectId = res.data.id;
          for (let i = 0; i < this.newRecord.images.length; i++) {
            let imageForm = new FormData();
            imageForm.append("project", projectId);
            imageForm.append("image", this.newRecord.images[i]);

            await axios.post("/api/v1/profile-project-image/", imageForm, {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            });
          }

          location.reload();
          this.$emit("close");
        })
        .catch((err) => {
          console.error(err);
        });
    },

    async updateProject(record) {
      let updateForm = { ...record };
      delete updateForm.id;
      axios
        .patch(`/api/v1/profile-project/${record.id}/`, updateForm)
        .then((res) => {
          location.reload();
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
        .post(`/api/v1/profile-project-image/`, formData)
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
          location.reload();
          this.$emit("close");
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async deleteProject(id) {
      console.log(id);
      axios
        .delete(`/api/v1/profile-project/${id}/`)
        .then(() => {
          this.$emit("deleted");
          location.reload();
          this.$emit("close");
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
