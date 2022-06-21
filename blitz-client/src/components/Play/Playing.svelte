<script lang="ts">
import { onDestroy, onMount } from "svelte";

    interface answer{
        answer_id: number | null
        answer_text: string
        correct: boolean
        question: number | null
    }

    interface selectedAnswer extends answer{
        selectedColour: string
    }

    onMount(() => {
        window.scrollTo(0, document.body.scrollHeight);
    })

    export let code:string;
    export let username;
    let points:number = 0;
    let answers:answer[] = [];
    let selectedAnswer:selectedAnswer | null = null;
    let showAnswers:boolean = false;
    let finished:boolean = false;
    let correctAnswer:boolean | null = null;

    let colours = ['#5BC0EB', '#FDE74C', '#4E4187', '#00CC66']

    const socket = new WebSocket(`ws://${window.location.host}/ws/group/${code}/`);

    socket.onopen = () => {
        socket.send(JSON.stringify({
            type: "user_joined",
            username: username,
            points: points,
        }));
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        switch (data.type) {
            case "user_joined":
                console.log(data)
                break;

            case "start_quiz":
                console.log(data)
                break;

            case "start_question":
                answers = data.answers;
                showAnswers = true;
                console.log(data)
                break;

            case "end_question":
                if(selectedAnswer.answer_id === data.answer){
                    points++;
                    correctAnswer = true;
                }
                else{
                    correctAnswer = false;
                }
                showAnswers = false;
                selectedAnswer = null;
                console.log(data)
                break;

            case "end_quiz":
                socket.send(JSON.stringify({
                    type: "score",
                    username: username,
                    points: points
                }));
                showAnswers = false;
                finished = true;
                console.log(data)
                break;
        };   
    };

    const selectAnswer = (answer:answer, colorIndex: number) => {
        selectedAnswer = {
            ...answer,
            selectedColour: colours[colorIndex]
        }
    }
    
    onDestroy(() => {
        socket.close();
    })

</script>

<main>

    {#if showAnswers}
        {#if selectedAnswer == null}
            <div class="answers">
                {#each answers as answer, index}
                    <div class="answer">
                        <div class="answer-inner" style="--bg-colour: {colours[index]};" on:click={() => selectAnswer(answer, index)}>{answer.answer_text}</div>
                    </div>
                {/each}
            </div>
        {:else if selectedAnswer != null}
            <div class="answer-selected" style="background-color: {selectedAnswer.selectedColour};">
                <div class="lds-ring"><div></div><div></div><div></div><div></div></div>
            </div>
        {/if}
    {:else if finished}
        <div>you got {points}</div>
    {:else}
        {#if correctAnswer}
            <div class="correct">
                <div class="circle"><div></div></div>
            </div>
        {:else if correctAnswer === false}
            <div class="incorrect">
                <div class="mdiv">
                    <div class="md"></div>
                </div>
            </div>
        {:else}
            <div>Waiting for question</div>
        {/if}
    {/if}

</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100%;
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
        height: 90%;
        width: 90%;
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

    .answer-inner:hover{
        cursor: pointer;
    }

    .correct{
        background-color: rgb(38, 198, 38);
        height: 100%;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .circle{
        height: 200px;
        width: 200px;
        background-color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .circle div{
        height: 70%;
        width: 70%;
        border-radius: 50%;
        background-color: rgb(38, 198, 38);
    }
    
    .incorrect{
        background-color: rgb(241, 28, 28);
        height: 100%;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .mdiv {
        height: 25%;
        width: 8px;
        margin-left: 12px;
        background-color: white;
        transform: rotate(45deg);
        Z-index: 1;
    }

    .md {
        height: 100%;
        width: 8px;
        background-color: white;
        transform: rotate(90deg);
        Z-index: 2;
    }

    .answer-selected{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        width: 100%;
    }

    .lds-ring {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 80px;
    }
    .lds-ring div {
    box-sizing: border-box;
    display: block;
    position: absolute;
    width: 64px;
    height: 64px;
    margin: 8px;
    border: 8px solid #fff;
    border-radius: 50%;
    animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    border-color: #fff transparent transparent transparent;
    }
    .lds-ring div:nth-child(1) {
    animation-delay: -0.45s;
    }
    .lds-ring div:nth-child(2) {
    animation-delay: -0.3s;
    }
    .lds-ring div:nth-child(3) {
    animation-delay: -0.15s;
    }
    @keyframes lds-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
    }
</style>