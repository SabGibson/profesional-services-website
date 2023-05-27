<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <div class="control">
        <button
          type="button"
          class="button is-link is-success"
          @click="newSkillRecord"
        >
          New Record
        </button>
        <h1>Edit Skills</h1>
        <div class="new-record-form" v-if="showModal">
          <form @submit.prevent="createNewRecord">
            <div class="field">
              <label class="label">Skill</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.skill_name"
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
          v-for="record in skills"
          v-bind:key="record.id"
          class="general-form"
        >
          <div class="field">
            <label class="label">Skill Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.skill_name}`"
                v-model="record.skill_name"
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

          <div class="field is-grouped">
            <div class="control">
              <button
                type="submit"
                class="button is-link"
                @click="updateCertification(record)"
              >
                Update
              </button>
            </div>
            <div class="control">
              <button
                type="button"
                class="button is-link is-danger"
                @click="deleteCertification(record.id)"
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
  name: "CertificationsModal",
  props: {
    skills: Object,
  },
  data() {
    return {
      showModal: false,
      newRecord: {
        skill_name: "",
        description: "",
      },
    };
  },
  methods: {
    newSkillRecord() {
      this.showModal = true;
      this.newRecord = {
        skill_name: "",
        description: "",
      };
    },

    async createNewRecord() {
      let form = this.newRecord;

      axios
        .post("/api/v1/profile-skill/", form)
        .then((res) => {
          this.newRecord = {
            certification_name: "",
            date_achieved: "",
            description: "",
          };
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async updateSkilkls(record) {
      let updateForm = { ...record };
      delete updateForm.id;

      axios
        .patch(`/api/v1/profile-skill/${this.record.id}/`, updateForm)
        .then((res) => {
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deleteSkills(id) {
      axios
        .delete(`/api/v1/profile-skill/${id}/`)
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
