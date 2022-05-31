<script>
import QuestionPage from "@/views/QuestionPage.vue";
import quizApiService from "@/services/quizApiService";

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
    created() {
        this.loadQuestionByPosition();
    },
    components: {
        QuestionPage,
    },
    methods: {
        async loadQuestionByPosition() {
            const res1 = await quizApiService.getQuestion(this.currentQuestionPosition);
            this.currentQuestion.image = res1.data.image;
            this.currentQuestion.title = res1.data.title;
            this.currentQuestion.text = res1.data.text;
            this.currentQuestion.possibleAnswers = res1.data.possibleAnswers;
            const res2 = await quizApiService.getQuizInfo();
            this.totalNumberOfQuestion = res2.data.size
        },
        async answerClickedHandler(selectedAnswerIndex) {
            this.answers.push(selectedAnswerIndex)
            this.currentQuestionPosition += 1;
            if (this.currentQuestionPosition === this.totalNumberOfQuestion) {
                this.endQuiz();
            } else {
                this.loadQuestionByPosition();
            }
        },
        async endQuiz() {
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