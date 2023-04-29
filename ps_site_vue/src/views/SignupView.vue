<template>
  <div class="page-sigup">
    <div class="columns is-multiline">
      <div class="column is-4 is-offset-4">
        <h1 class="title has-text-centered">Sign up</h1>
        <form @submit.prevent="submitform">
          <div class="field">
            <label for="">Username</label>
            <div class="control">
              <input type="text" class="input" v-model="username" />
            </div>
          </div>
          <div class="field">
            <label for="">Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password" />
            </div>
          </div>
          <div class="field">
            <label for="">Confirm Password</label>
            <div class="control">
              <input type="password" class="input" v-model="password2" />
            </div>
          </div>
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Sign up</button>
            </div>
          </div>

          <hr />

          Or <router-link to="/log-in">click here</router-link> to log in!
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "Signup",

  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  components: {},
  mounted() {
    document.title = document.title = "Sign-up" + " | Grünluft";
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (this.username === "") {
        this.errors.push("The username is missing");
      }

      if (this.password !== this.password2) {
        this.errors.push("The passwords doesn't match");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };

        axios
          .post("/api/v1/users/", formData)
          .then((res) => {
            toast({
              message: "Account created successfully,proceed to login",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            this.$router.push("/log-in");
          })
          .catch((err) => {
            if (err.response) {
              for (const prop in err.response.data) {
                this.errors.push(`${prop}: ${err.response.data[prop]}`);
              }

              console.log(JSON.stringify(err.response.data));
            } else if (err.message) {
              this.errors.push("Something went werong.Please try again");
              console.log(JSON.stringify(err));
            }
          });
      }
    },
  },
};
</script>
