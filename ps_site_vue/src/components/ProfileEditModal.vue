<template>
  <div class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-content box">
      <h2>Edit Profile</h2>
      <form @submit.prevent="updateUser('first_name')">
        <div class="field">
          <label class="label">First Name</label>
          <input class="input" v-model="profile.first_name" type="text" />
          <button class="button is-link">Save Changes</button>
        </div>
      </form>
      <form @submit.prevent="updateUser('last_name')">
        <div class="field">
          <label class="label">Last Name</label>
          <input class="input" v-model="profile.last_name" type="text" />
          <button class="button is-link">Save Changes</button>
        </div>
      </form>
      <form @submit.prevent="updateProfile('bio')">
        <div class="field">
          <label class="label">Bio</label>
          <textarea class="textarea" v-model="profile.bio"></textarea>
          <button class="button is-link">Save Changes</button>
        </div>
      </form>
      <form @submit.prevent="updateProfile('image')">
        <div class="field">
          <label class="label">Profile Image</label>
          <input type="file" @change="onFileChange" />
          <button class="button is-link">Save Changes</button>
        </div>
      </form>
      <div class="control">
        <button class="button is-link" type="button" @click="closeModal">
          Cancel
        </button>
      </div>
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
      originalProfile: this.profile ? { ...this.profile } : {},
    };
  },
  methods: {
    closeModal() {
      this.$emit("close");
    },
    onFileChange(e) {
      this.selectedFile = e.target.files[0];
    },

    async updateUser(field) {
      let formData = new FormData();

      if (this.profile[field] !== this.originalProfile[field]) {
        formData.append(field, this.profile[field]);
      }

      axios
        .patch(`/api/v1/users/me/`, formData)
        .then((res) => {
          this.closeModal();
          location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async updateProfile(field) {
      let formData = new FormData();

      if (this.profile[field] !== this.originalProfile[field]) {
        formData.append(field, this.profile[field]);
      }

      if (field === "image" && this.selectedFile) {
        formData.append("image", this.selectedFile);
      }

      axios
        .patch(`/api/v1/profiles/${this.profile.id}/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((res) => {
          this.closeModal();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
