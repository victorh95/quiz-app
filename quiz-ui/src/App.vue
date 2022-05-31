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
.navbar-custom {
  height: 60px;
}
</style>
