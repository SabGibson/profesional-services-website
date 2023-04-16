<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"
          ><strong>GurunLuft</strong></router-link
        >
        <a
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          class="navbar-burger"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link to="/store" class="navbar-item">Store</router-link>
          <router-link to="/gallery" class="navbar-item">Gallery</router-link>
          <router-link to="/profile" class="navbar-item">Profile</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light"
                >Login</router-link
              >
              <router-link to="/cart" class="button is-success">
                <span class="icon">
                  <i class="fa-cart-shopping"></i>
                </span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-right">Copyrigth (c) 2023</p>
    </footer>
  </div>
</template>

<style lang="scss">
@import "../node_modules/bulma";
</style>
