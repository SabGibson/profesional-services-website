<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <div class="control">
        <button
          type="button"
          class="button is-link is-success"
          @click="newEducationRecord"
        >
          New Record
        </button>
        <h1>Edit Education</h1>
        <div class="new-record-form" v-if="showModal">
          <form @submit.prevent="createNewRecord">
            <div class="field">
              <label class="label">Institution Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.institution_name"
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
              <label class="label">Qualification Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.qualification_name"
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
              <label class="label">Date Achieved</label>
              <div class="control">
                <input
                  class="input"
                  type="date"
                  v-model="this.newRecord.date_achieved"
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
          v-for="(record, idx) in education"
          v-bind:key="record.id"
          class="general-form"
        >
          <div class="field">
            <label class="label">Institution Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.institution_name}`"
                v-model="record.institution_name"
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
            <label class="label">Qualification Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.qualification_name}`"
                v-model="record.qualification_name"
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
            <label class="label">Date Achieved</label>
            <div class="control">
              <input
                class="input"
                type="date"
                :placeholder="`${record.date_achieved}`"
                v-model="record.date_achieved"
              />
            </div>
          </div>
          <div class="field is-grouped">
            <div class="control">
              <button
                type="submit"
                class="button is-link"
                @click="updateEducation(record)"
              >
                Update
              </button>
            </div>
            <div class="control">
              <button
                type="button"
                class="button is-link is-danger"
                @click="deleteEducation(record.id)"
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
  name: "EducationModal",
  props: {
    education: Object,
  },
  data() {
    return {
      showModal: false,
      newRecord: {
        institution_name: "",
        level: "",
        qualification_name: "",
        description: "",
        date_achieved: "",
      },
    };
  },
  methods: {
    newEducationRecord() {
      this.showModal = true;
      this.newRecord = {
        institution_name: "",
        level: "",
        qualification_name: "",
        description: "",
        date_achieved: "",
      };
    },

    async createNewRecord() {
      let form = this.newRecord;

      axios
        .post("/api/v1/profile-education/", form)
        .then((res) => {
          this.newRecord = {
            institution_name: "",
            level: "",
            qualification_name: "",
            description: "",
            date_achieved: "",
          };
          location.reload();
          this.$emit("close");
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async updateEducation(record) {
      let updateForm = { ...record };
      delete updateForm.id;
      console.log("clicked");
      axios
        .patch(`/api/v1/profile-education/${record.id}/`, updateForm)
        .then((res) => {
          location.reload();
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    },

    async deleteEducation(id) {
      axios
        .delete(`/api/v1/profile-education/${id}/`)
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
