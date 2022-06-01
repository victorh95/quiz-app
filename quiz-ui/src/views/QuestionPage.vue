<script>
export default {
    props: {
        question: {
            type: Object
        }
    },
    emits: ["answer-selected"]
}
</script>

<template>
    <div class="center">
        <img v-if="question.image" :src="question.image" height="300" />
        <h2>{{ question.title }}</h2>
        <p>{{ question.text }}</p>
        <div class="fd-row mb-3">
            <button v-for="(possibleAnswer, index) in question.possibleAnswers" v-bind:key="possibleAnswer"
                @click="$emit('answer-selected', index)" type="button" class="btn btn-primary mx-3 btn-custom">
                {{ possibleAnswer.text }}
            </button>
        </div>
    </div>
</template>

<style>
.center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.fd-row {
    display: flex;
    flex-direction: row;
}
</style>
