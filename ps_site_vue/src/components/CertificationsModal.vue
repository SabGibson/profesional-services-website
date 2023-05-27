<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <div class="control">
        <button
          type="button"
          class="button is-link is-success"
          @click="newCertificationRecord"
        >
          New Record
        </button>
        <h1>Edit Certification</h1>
        <div class="new-record-form" v-if="showModal">
          <form @submit.prevent="createNewRecord">
            <div class="field">
              <label class="label">Certification Name</label>
              <div class="control">
                <input
                  class="input"
                  type="text"
                  v-model="this.newRecord.certification_name"
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
          v-for="record in certifications"
          v-bind:key="record.id"
          class="general-form"
        >
          <div class="field">
            <label class="label">Certification Name</label>
            <div class="control">
              <input
                class="input"
                type="text"
                :placeholder="`${record.certification_name}`"
                v-model="record.certification_name"
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
    certifications: Object,
  },
  data() {
    return {
      showModal: false,
      newRecord: {
        certification_name: "",
        date_achieved: "",
        description: "",
      },
    };
  },
  methods: {
    newCertificationRecord() {
      this.showModal = true;
      this.newRecord = {
        certification_name: "",
        date_achieved: "",
        description: "",
      };
    },

    async createNewRecord() {
      let form = this.newRecord;

      axios
        .post("/api/v1/profile-certification/", form)
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
    async updateCertification(record) {
      let updateForm = { ...record };
      delete updateForm.id;

      axios
        .patch(`/api/v1/profile-certification/${this.record.id}/`, updateForm)
        .then((res) => {
          this.$emit("close");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async deleteCertification(id) {
      axios
        .delete(`/api/v1/profile-certification/${id}/`)
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
