<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <form @submit.prevent="updateEducation">
        <div
          v-for="(record, idx) in experience"
          v-bind:key="record.id"
          class="general-form"
        >
          <div class="field">
            <label class="label">Company Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.company_name}`"
                v-model="record.company_name"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Job Title</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.job_title}`"
                v-model="record.job_title"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Level</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.level}`"
                v-model="record.level"
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
          <div class="field">
            <label class="label">Date Started</label>
            <div class="control">
              <input
                class="input"
                type="date"
                :placeholder="`${record.date_started}`"
                v-model="record.date_started"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Date Ended</label>
            <div class="control">
              <input
                class="input"
                type="date"
                :placeholder="`${record.date_ended}`"
                v-model="record.date_ended"
              />
            </div>
          </div>
          <div class="field">
            <label class="label">Current Role</label>
            <div class="control">
              <input
                class="input"
                type="boolean"
                :placeholder="`${record.is_present}`"
                v-model="record.is_present"
              />
            </div>
          </div>

          <div class="field is-grouped">
            <div class="control">
              <button
                type="submit"
                class="button is-link"
                @click="updateExperience(record)"
              >
                Update
              </button>
            </div>
            <div class="control">
              <button
                type="button"
                class="button is-link is-danger"
                @click="deleteExperience(record.id)"
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
  name: "ExperienceModal",
  props: {
    experience: Object,
  },
  data() {
    return {};
  },
  methods: {
    async updateExperience(record) {
      console.log(record);
      // axios
      //   .patch(
      //     `/api/v1/profile-education/${this.record.id}/`,
      //     this.updatedEducation
      //   )
      //   .then((res) => {
      //     this.$emit("close");
      //   })
      //   .catch((err) => {
      //     console.log(err);
      //   });
    },
    async deleteExperience(id) {
      console.log(id);
      // axios
      //   .delete(`/api/v1/profile-education/${id}/`)
      //   .then(() => {
      //     this.$emit("deleted");
      //   })
      //   .catch((err) => {
      //     console.error(err);
      //   });
    },
  },
};
</script>
