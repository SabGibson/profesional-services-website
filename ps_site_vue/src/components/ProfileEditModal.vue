<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <h2>Edit Profile</h2>
      <form @submit.prevent="updateProfile">
        <div class="field">
          <label class="label">First Name</label>
          <input class="input" v-model="profile.first_name" type="text" />
        </div>
        <div class="field">
          <label class="label">Last Name</label>
          <input class="input" v-model="profile.last_name" type="text" />
        </div>
        <div class="field">
          <label class="label">Bio</label>
          <textarea class="textarea" v-model="profile.bio"></textarea>
        </div>
        <div class="field">
          <label class="label">Profile Image</label>
          <input type="file" @change="onFileChange" />
        </div>
        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link">Save Changes</button>
          </div>
          <div class="control">
            <button class="button is-link" type="button" @click="closeModal">
              Cancel
            </button>
          </div>
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
  name: "EditProfileModal",
  props: {
    profile: Object,
  },
  data() {
    return {
      showModal: false,
      selectedFile: null,
    };
  },
  methods: {
    closeModal() {
      this.$emit("close");
    },
    onFileChange(e) {
      this.selectedFile = e.target.files[0];
    },
    updateProfile() {
      let formData = new FormData();
      formData.append("first_name", this.profile.first_name);
      formData.append("last_name", this.profile.last_name);
      formData.append("bio", this.profile.bio);
      if (this.selectedFile) {
        formData.append("image", this.selectedFile);
      }

      axios
        .put(`/api/v1/profiles/${this.profile.id}/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          this.showModal = false;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
