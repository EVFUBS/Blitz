<script lang="ts">
import { onDestroy, onMount } from "svelte";
import { csrf } from "../../store";

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

    export let session: question[];
    let currentQuestion: question | null = null;
    let QuestionNumber: number = 0;
    let play:boolean | null = null;
    let users = [];
    let userScores = [];
    let timer;

    let colours = ['#5BC0EB', '#FDE74C', '#4E4187', '#00CC66']

    //random num between 100000 and 999999
    let random_code: string = (Math.floor(Math.random() * (999999 - 100000 + 1)) + 100000).toString();
    const socket = new WebSocket(`ws://${window.location.host}/ws/group/${random_code}/`);

    onMount(() => {
        window.scrollTo(0, document.body.scrollHeight);
    })

    socket.onopen = () => {
        console.log("connected");
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        switch (data.type) {
            case "user_joined":
                delete data.type;
                users = [...users, data];
                console.log(users);
                break;

            case "user_score":
                delete data.type;
                userScores = [...userScores, data];
                console.log(userScores);
                break;
        }
    }

    const startQuiz = () => {
        if (users.length >= 1) {
            play = true;
            socket.send(JSON.stringify({
                type: "start_quiz",
            }));
            startQuestion();
        }
        else{
            alert("Not enough players to start quiz");
        }    
    }

    const startQuestion = () => {
        clearInterval(timer);
        currentQuestion = session[QuestionNumber];
        QuestionNumber++;
        socket.send(JSON.stringify({
            type: "start_question",
            answers: currentQuestion.answers,
        }));
        timer = setInterval(() => {
            socket.send(JSON.stringify({
                type: "end_question",
                answer: currentQuestion.answers.find(answer => answer.correct).answer_id,
            }));
            endQuestion();
        }, 10000);
    }

    const endQuestion = () => {
        clearInterval(timer);
        currentQuestion = {
            question_id: null,
            question_text: "Next Question...",
            group_id: null,
            answers: [],
        };
        timer = setInterval(() => {
            if (QuestionNumber < session.length) {
                startQuestion();
            } else {
                endQuiz();
            }
        }, 5000);
    }

    const endQuiz = () => {
        clearInterval(timer);
        play = false;
        socket.send(JSON.stringify({
            type: "end_quiz",
        }));
    }

    onDestroy(() => {
        socket.close();
    });

</script>

<main>
    {#if play}
        <div class="quiz">
            <h1>{currentQuestion.question_text}</h1>
            <div class="answers">
                {#each currentQuestion.answers as answer, index}
                    <div class="answer">
                        <div class="answer-inner" style="--bg-colour: {colours[index]};">{answer.answer_text}</div>
                    </div>
                {/each}
            </div>
        </div>
    {:else if play === false}
        <div class="finished">
            <h1>Quiz Finished</h1>
            <div>
                {#each userScores as user}
                    <div class="scores">{user.username} - {user.points}</div>
                {/each}
            </div>
        </div>
    {:else}
        <div class="start">
            <p>Enter the Session code to join</p>
            <h2 class="code">{random_code}</h2>
            {#each users as user}
                <p>{user.username}</p>
            {/each}
            <button on:click={() => startQuiz()}>start</button>
        </div>
    {/if}

</main>

<style>

    main {
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: 100%;
    }

    .start{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100%;

    }

    .quiz{
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100vh;
        width: 100%;
        text-align: center;
    }

    .finished{
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: 100%;
        text-align: center;
    }

    .scores{
        font-size: large;
    }

    .answers{
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 10px;
        height: 100%;
        width: 100%;
    }

    .answer{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

    }

    .answer-inner{
        height: 95%;
        width: 95%;
        border-radius: 2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        color: black;
        font-size: 1.3rem;
        color: white;
        background-color: var(--bg-colour);
        box-shadow: 1px 3px 3px 1px rgba(0,0,0,0.2);
    }

    .code{
        text-align: center;
    }

    button{
        color: #0070f3;
        border: #0070f3 solid 2px;
        border-radius: 5px;
        text-decoration: none;
        font-family: monospace;
        font-size: 0.9rem;
        font-weight: bold;
        padding: 0.5rem;
        transition: 0.2s;
        background-color: white;
        height: 40px;
        width: 200px;
    }

    button:hover{
        background-color: #0070f3;
        color: white;
    }


</style>