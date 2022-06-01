<script>
import QuestionPage from "@/views/QuestionPage.vue";
import quizApiService from "@/services/quizApiService";
import participationStorageService from "@/services/participationStorageService";

export default {
    data() {
        return {
            currentQuestion: {
                image: "",
                title: "",
                text: "",
                possibleAnswers: [],
            },
            currentQuestionPosition: 1,
            totalNumberOfQuestion: null,
            answers: [],
        };
    },
    async created() {
        const res = await quizApiService.getQuizInfo();
        this.totalNumberOfQuestion = res.data.size
        this.loadQuestionByPosition();
    },
    components: {
        QuestionPage,
    },
    methods: {
        async loadQuestionByPosition() {
            const res = await quizApiService.getQuestion(this.currentQuestionPosition);
            this.currentQuestion.image = res.data.image;
            this.currentQuestion.title = res.data.title;
            this.currentQuestion.text = res.data.text;
            this.currentQuestion.possibleAnswers = res.data.possibleAnswers;
        },
        async answerClickedHandler(selectedAnswerIndex) {
            const selectedAnswerPosition = selectedAnswerIndex + 1
            this.answers.push(selectedAnswerPosition)
            if (this.currentQuestionPosition === this.totalNumberOfQuestion) {
                this.endQuiz();
            } else {
                this.currentQuestionPosition += 1;
                this.loadQuestionByPosition();
            }            
        },
        async endQuiz() {
            const playerName = participationStorageService.getPlayerName();
            const res = await quizApiService.postParticipation(playerName, this.answers)
            participationStorageService.saveParticipationScore(res.data.score);
            this.$router.push('/score');
        }
    }
};
</script>

<template>
    <h1 class="mb-3 center">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <QuestionPage :question="currentQuestion" @answer-selected="answerClickedHandler" />
</template>

<style>
.center {
    margin: auto;
}
</style>