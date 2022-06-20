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

    //random num between 100000 and 999999
    let random_code: string = (Math.floor(Math.random() * (999999 - 100000 + 1)) + 100000).toString();
    const socket = new WebSocket(`ws://127.0.0.1:8000/ws/group/${random_code}/`);

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
        <div>
            <h1>{currentQuestion.question_text}</h1>
            <div>
                {#each currentQuestion.answers as answer}
                    <div>{answer.answer_text}</div>
                {/each}
            </div>
        </div>
    {:else if play === false}
        <div>
            <h1>Quiz Finished</h1>
            <div>
                {#each userScores as user}
                    <div>{user.username} - {user.points}</div>
                {/each}
            </div>
        </div>
    {:else}
        <p>Enter the Session code to join</p>
        <h2>{random_code}</h2>
        {#each users as user}
            <p>{user.username}</p>
        {/each}
        <button on:click={() => startQuiz()}>start</button>
    {/if}

</main>

<style>

</style>