<script>
import quizApiService from "@/services/quizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    const res = await quizApiService.getQuizInfo();
    this.registeredScores = res.data.scores
  }
};
</script>

<template>
  <h1>Page d'accueil</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.id">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <RouterLink to="/new-quiz">Commencer le quiz</RouterLink>
</template>