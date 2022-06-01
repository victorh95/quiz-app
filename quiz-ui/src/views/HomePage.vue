<script>
import quizApiService from "@/services/quizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [],
    };
  },
  async created() {
    const res = await quizApiService.getQuizInfo();
    this.registeredScores = res.data.scores
  }
};
</script>

<template>
  <div class="text-center">
    <h2 class="mt-3 mb-5">🏆 Tableau des scores 🏆</h2>
    <div class="scoreboard">
      <span v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.id" class="mb-3">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
      </span>
    </div>
    <h2 class="mb-5">🎮 Jouez pour apparaître sur le tableau 🎮</h2>
    <a href="/new-quiz"><button type="button" class="btn btn-primary mb-3 btn-custom ">Commencer le quiz</button></a>
  </div>
</template>

<style>
.scoreboard {
  height: 300px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}
</style>