<template>
  <div class="page-login">
    <div class="columns is-multiline">
      <div class="column is-4 is-offset-4">
        <h1 class="title has-text-centered">Login</h1>
        <form @submit.prevent="submitForm">
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
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-dark">Login</button>
            </div>
          </div>

          <hr />

          Or <router-link to="/sign-up">click here</router-link> to sign up!
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "Login",

  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  components: {},
  mounted() {
    document.title = document.title = "Login" + " | Grünluft";
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("/api/v1/token/login/", formData)
        .then(async (res) => {
          const token = res.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          const userRes = await axios.get("/api/v1/users/me/");
          this.$store.commit("setUser", userRes.data);
          localStorage.setItem("user_id", userRes.data.id);
          localStorage.setItem("profile_id", userRes.data.profile.id);
          const toPath = this.$route.query.to || "/basket";
          this.$router.push(toPath);
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
    },
  },
};
</script>
