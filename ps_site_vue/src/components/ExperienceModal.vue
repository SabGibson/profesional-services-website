<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <div class="control">
        <button
          type="button"
          class="button is-link is-success"
          @click="newExperienceRecord"
        >
          New Record
        </button>
        <h1>Edit Experience</h1>
        <div class="new-record-form" v-if="showModal">
          <form @submit.prevent="createNewRecord">
            <div class="field">
              <label class="label">Company Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.company_name"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Level</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.level"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Job Title</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.job_title"
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
              <label class="label">Date Started</label>
              <div class="control">
                <input
                  class="input"
                  type="date"
                  v-model="this.newRecord.date_started"
                />
              </div>
            </div>
            <div class="field">
              <label class="label">Date Endeded</label>
              <div class="control">
                <input
                  class="input"
                  type="date"
                  v-model="this.newRecord.date_endeded"
                />
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label class="checkbox">
                  Is Current?
                  <input type="checkbox" v-model="this.newRecord.is_current" />
                </label>
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
            <div class="control">
              <label class="checkbox">
                Is Current?
                <input type="checkbox" v-model="this.newRecord.is_current" />
              </label>
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
    return {
      showModal: false,
      newRecord: {
        company_name: "",
        level: "",
        job_title: "",
        description: "",
        date_started: "",
        date_endeded: "",
        is_present: "",
      },
    };
  },
  methods: {
    newExperienceRecord() {
      this.showModal = true;
      this.newRecord = {
        company_name: "",
        level: "",
        job_title: "",
        description: "",
        date_started: "",
        date_endeded: "",
        is_present: "",
      };
    },
    async createNewRecord() {
      let form = this.newRecord;

      axios
        .post("/api/v1/profile-employment", form)
        .then((res) => {
          this.newRecord = {
            company_name: "",
            level: "",
            job_title: "",
            description: "",
            date_started: "",
            date_endeded: "",
            is_present: "",
          };
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async updateExperience(record) {
      let updateForm = { ...record };
      delete updateForm.id;

      axios
        .patch(`/api/v1/profile-employment/${this.record.id}/`, updateForm)
        .then((res) => {
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deleteExperience(id) {
      axios
        .delete(`/api/v1/profile-employment/${id}/`)
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
