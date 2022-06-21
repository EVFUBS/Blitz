<script lang="ts">
    import { onMount } from "svelte";
    import { csrf } from "../../store";
import Session from "./Session.svelte";

    interface groupProps {
        group_id: number | null;
        group_name: string;
        group_description: string;
        category_id: number | null;
        author: number | null;
    }

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

    interface author{
        id: number | null
        username: string
        email: string
        date_joined: string
        last_login: string
    }
    
    export let group:groupProps;
    let qa: question[] = [];
    let session: question[] | undefined;
    let author: author;

    onMount(async() => {
        const response = await fetch(`/api/quiz/questions/answers/${group.group_id}`, {
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

    onMount(async() => {
        const response = await fetch(`/api/auth/users/${group.author}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            }
        });
        const data = await response.json();
        author = data;
    });
    
</script>

<main>
    {#if session !== undefined}
        <Session session={session} />
    {:else}
        {#await qa}
            <p>waiting...</p>
        {:then qa}
            <div class="group">
                <div class="quiz">
                    <h3>{group.group_name}</h3>
                    <p>{group.group_description}</p>
                    {#if author !== undefined}
                        <p>Author: {author.username}</p>
                    {:else}
                        <p>Author: unknown</p>
                    {/if}
                </div>
                <div class="questions">
                    <p>{qa.length} questions</p>
                    {#each qa as question}
                        <div class="question">
                           <details>
                                <summary>{question.question_text}</summary>
                                <ul class="answers">
                                    {#each question.answers as answer}
                                        <li class="answer">{answer.answer_text}</li>
                                    {/each}
                                </ul>
                           </details> 
                        </div>
                        
                    {/each}
                    <button on:click={() => session = qa}>Play</button>
                </div>
            </div>
        {/await}
    {/if}
</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
    }
    
    .group{
        display: flex;
        flex-direction: row;
        justify-content: space-between;;
        width: 100%;
        height: 100%;
    }

    @media (max-width: 768px) {
        .group{
            align-items: center;
            flex-direction: column;
        }
    }

    .quiz{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 50%;
        height: 100%;
    }

    .questions{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 50%;
    }

    @media (max-width: 768px) {
        .questions{
            width: 90%;
        }
    }

    .question{
        margin-bottom: 1rem;
        width: 90%;
    }

    @media (max-width: 768px) {
        .question{
            width: 100%;
        }
    }

    details {
        border: 1px solid #aaa;
        border-radius: 4px;
        padding: .5em .5em 0;
    }

    summary {
        font-weight: bold;
        margin: -.5em -.5em 0;
        padding: .5em;
        width: 100%;
        cursor: pointer;
    }

    details[open] {
        padding: .5em;
    }

    details[open] summary {
        border-bottom: 1px solid #aaa;
        margin-bottom: .5em;
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
        width: 90%;
    }

    @media (max-width: 768px) {
        button{
            width: 100%;
        }
    }

    button:hover{
        background-color: #0070f3;
        color: white;
    }


</style>