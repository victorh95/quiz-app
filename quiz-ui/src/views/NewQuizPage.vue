<script>
import participationStorageService from "@/services/participationStorageService";

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: ""
    };
  },
  methods: {
    launchNewQuiz(){
      if(this.username == ""){
        this.username = "Anonyme"
      }
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/questions');
    },
  }
};
</script>

<template>
  <div class="center-container">
    <div>
      <div class="mb-3 width-300px">
        <label class="form-label">Saisissez votre nom :</label>
        <input v-model="username" type="text" class="form-control" placeholder="Nom d'utilisateur">
      </div>
      <button @click="launchNewQuiz" type="button" class="btn btn-primary width-300px">Commencer le quiz</button>
    </div>
  </div>
</template>

<style>
</style>