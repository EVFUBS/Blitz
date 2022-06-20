<script lang="ts">
import { onMount } from "svelte";
import Question from "./Question.svelte";
import { csrf } from "../../store";

    export let group_id: number;
    export let unSelectGroup: () => void;
    let qa: question[] = [];

    onMount(async() => {
        const response = await fetch(`/api/quiz/questions/answers/${group_id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            }
        });
        const data = await response.json();
        qa = data;
        console.log(qa);
    });

    interface question {
        question_id: number | null;
        question_text: string
        group_id: number | null
        answers: answer[]
    }

    interface answer {
        answer_id: number | null
        answer_text: string
        correct: boolean
        question: number | null
    }

    const addNewAnswer = (question: question) => {
        if(question.answers.length < 4) {
            question.answers.push({
                answer_id: null,
                answer_text: "",
                correct: false,
                question: question.question_id
            });
            qa = [...qa];
            console.log(question);
        }
    };

    const addNewQuestion = () => {
        qa.push({
            question_id: null,
            question_text: "",
            group_id: group_id,
            answers: []
        });
        qa = [...qa];
        console.log(qa);
    };

    const submitQuestions = async() => {
        const response = await fetch(`/api/quiz/questions/answers/${group_id}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            },
            body: JSON.stringify(qa)
        });
        if(response.status === 201) {
            console.log("Questions submitted");
            unSelectGroup();
        }
        else{
            console.log("Questions not submitted");
        }
    };

    const deleteQuestion = async(question: question, index: number) => {
        if(question.question_id === null) {
            qa.splice(index, 1);
            qa = [...qa];
        }
        else{
            await fetch(`/api/quiz/questions/${question.question_id}`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": $csrf
                }
            });
            qa.splice(index, 1);
            qa = [...qa];
            console.log("server");
        }
    }

    const deleteAnswer = (question: question, answer: answer, index: number) => {
        if(answer.answer_id === null) {
            question.answers.splice(index, 1);
            qa = [...qa];
        }
        else{
            fetch(`/api/quiz/answers/${answer.answer_id}`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": $csrf
                }
            });
            question.answers.splice(index, 1);
            qa = [...qa];
            console.log("server");
        }
    }
</script>

<main>
    {#await qa}
        <p>getting questions</p>
    {:then qa}
        <form>
            {#each qa as question, questionIndex}
                <div class="question">
                    <div>
                        <input type="text" bind:value={question.question_text}>
                        <button on:click|preventDefault={() => deleteQuestion(question, questionIndex)}>-</button>
                    </div>
                    {#each question.answers as answer, answerIndex}
                        <div>
                            <input type="text" bind:value={answer.answer_text}>
                            <input type="checkbox" name="correct" id="" bind:checked={answer.correct}>
                            <button on:click|preventDefault={() => deleteAnswer(question, answer, answerIndex)}>-</button>
                        </div>
                    {/each}
                    {#if question.answers.length < 4}
                        <button on:click|preventDefault={() => addNewAnswer(question)}>+</button>
                    {/if}
                </div>
            {/each}
            <div>
                <button on:click|preventDefault={() => addNewQuestion()}>new question</button>
                <button on:click|preventDefault={() => submitQuestions()}>submit</button>
            </div>
        </form>
    {/await}
</main>

<style>
    main form{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
    }

    .question{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.5rem;
    }

</style>