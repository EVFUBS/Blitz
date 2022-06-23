<script lang="ts">
import { onMount } from "svelte";
import Question from "./Question.svelte";
import { csrf } from "../../store";
import Button from "../General/Button.svelte";

    export let group_id: number;
    export let unSelectGroup: () => void;
    let qa: question[] = [];
    let colours = ['#5BC0EB', '#FDE74C', '#4E4187', '#00CC66']

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
        for(let question of qa){
            if(question.question_text[question.question_text.length - 1] != "?") {
                question.question_text += "?";
            }
        }
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
            alert("Questions submitted");
            unSelectGroup();
        }
        else{
            console.log("Questions not submitted");
        }
    };

    const deleteQuestion = async(question: question, index: number) => {
        if(confirm("Are you sure you want to delete this question?")){
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
        <form on:submit|preventDefault>
            {#each qa as question, questionIndex}
                <div class="question">
                    <div class="question-info">
                        <input class="question-text" type="text" placeholder="Enter a question" bind:value={question.question_text}>
                        <div></div>
                        <button class="redButton" on:click={() => deleteQuestion(question, questionIndex)}>-</button>
                    </div>
                    {#each question.answers as answer, answerIndex}
                        <div class="answers" style="--question-colour: {colours[answerIndex]};">
                            <input class="answer-text" type="text" placeholder="answer" bind:value={answer.answer_text}>
                            <input type="checkbox" name="correct" id="" bind:checked={answer.correct}>
                            <button class="redButton" on:click={() => deleteAnswer(question, answer, answerIndex)}>-</button>
                        </div>
                    {/each}
                    {#if question.answers.length < 4}
                        <Button content="+" on:click={() => addNewAnswer(question)}/>
                    {/if}
                </div>
            {/each}
            <div class="options">
                <Button content="New Question" on:click={() => addNewQuestion()}>new question</Button>
            </div>
        </form>
        <Button content="Submit" on:click={() => submitQuestions()}>submit</Button>
    {/await}
</main>

<style>
    main{
        width: 80%;
        margin: 1rem;
    }

    main form{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-bottom: 2rem;
    }

    @media (max-width: 768px) {
        main form{
            grid-template-columns: 1fr;
        }
    }

    .question{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
        height: 250px;
        width: 100%;
    }

    .question-info{
        width: 100%;
        display: grid;
        grid-template-columns: 10fr 1fr 1fr;
    }

    .question-text{
        font-size: 1.1rem;
        box-sizing: border-box;
    }

    .answers{
        width: 100%;
        display: grid;
        grid-template-columns: 10fr 1fr 1fr;
    }

    .answer-text{
        font-size: 0.9rem;
        border: 2px solid var(--question-colour);
    }

    .answer-text:focus{
        outline: 2px solid var(--question-colour);
    }

    .options{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }

</style>