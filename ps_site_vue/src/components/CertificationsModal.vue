<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
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
    return {};
  },
  methods: {
    async updateCertification(record) {
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
    async deleteCertification(id) {
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
