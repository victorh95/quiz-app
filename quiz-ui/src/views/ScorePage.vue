<script>
import participationStorageService from "@/services/participationStorageService";
import quizApiService from "@/services/quizApiService";

export default {
    name: "ScorePage",
    data() {
        return {
            score: participationStorageService.getParticipationScore(),
            registeredScores: [],
            position: null,
            totalNumberOfQuestion: null,
        };
    },
    async created() {
        const res = await quizApiService.getQuizInfo();
        this.registeredScores = res.data.scores
        this.totalNumberOfQuestion = res.data.size
        const namesPlayers = []
        for (let i = 0; i < this.registeredScores.length; i++) {
            namesPlayers.push(this.registeredScores[i].playerName)
        }
        const playerName = participationStorageService.getPlayerName();
        this.position = namesPlayers.indexOf(playerName) + 1;
    }
};
</script>

<template>
    <div class="text-center">
        <h1 v-if="score == 10" class=" mt-3 mb-3">🎊 Bravo, vous avez obtenu un score de {{ score }} / 10 🎊</h1>
        <div v-else class="mt-3 mb-3">
            <h1>💪 Vous avez obtenu un score de {{ score }} / {{ totalNumberOfQuestion }} 💪</h1>
            <h2>Retentez votre chance pour peut-être obtenir la note maximale !</h2>
        </div>
        <h2 class="mb-2">🏆 Tableau des scores 🏆</h2>
        <h3>Votre position : {{ position }}</h3>
        <div class="scoreboard">
            <span v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.id" class="mb-3">
                {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
            </span>
        </div>
        <div class="fd-column">
            <a href="/new-quiz"><button type="button" class="btn btn-primary mb-3 btn-custom">Recommencer</button></a>
            <a href="/"><button type="button" class="btn btn-primary mb-3 btn-custom ">Page d'accueil</button></a>
        </div>
    </div>
</template>

<style>
</style>
