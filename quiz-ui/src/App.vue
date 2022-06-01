<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark navbar-custom">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img src="@/assets/logo.svg" alt="" width="30" height="30">
          Vue quiz
        </a>
        <div class="collapse navbar-collapse">
          <div class="navbar-nav">
            <RouterLink class="nav-link" to="/">Page d'accueil</RouterLink>
            <RouterLink class="nav-link" to="/admin">Administration</RouterLink>
          </div>
        </div>
      </div>
    </nav>
  </header>
  <div class="container">
    <RouterView />
  </div>
</template>

<style>
h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: normal;
}

.navbar-custom {
  height: 60px;
}

.center-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 60px);
}

.btn-custom {
  width: 200px;
}

.width-300px {
  width: 300px;
}

.fd-column {
  display: flex;
  flex-direction: column;
}
</style>
