<script lang="ts">
import { onMount } from "svelte";


    export let question
    let question_text = ""
    let answer_text = ""
</script>

<main>
    <input type="text" name="question_text" id="" bind:value={question.question_text} on:change={() => console.log(question)}>
    {#each question.answers as answer}
        <input type="text" name="answer_text" id="" bind:value={answer.answer_text}>
    {/each}
</main>

<style>

    main{
        margin: 20px;
    }

    main{
        display: flex;
        flex-direction: column;
        align-items: center;
    }

</style>