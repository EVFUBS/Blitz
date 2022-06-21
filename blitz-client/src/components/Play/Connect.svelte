<script lang="ts">
import { onMount } from "svelte";

    import Playing from "./Playing.svelte";

    export let code: string;
    let username:string;
    let usernameEntered:boolean = false;

    onMount(() => {
        window.scrollTo(0, document.body.scrollHeight);
    })

</script>

<main>
    {#if usernameEntered}
        <Playing code={code} username={username}/>
    {:else}
        <p>Enter username</p>
        <form on:submit|preventDefault>
            <input type="text" bind:value={username}>
            <button type="submit" on:click={() => usernameEntered = true}>></button>
        </form>
    {/if}

</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100vh;
    }

    form{
        display: flex;
        flex-direction: row;
        justify-content: center;
        width: 90%;
        height: 60px;
    }

    form input{
        width: 300px;
        border-radius: 5px 0 0 5px;
        border: 2px solid #0070f3;
        font-size: larger;
        text-align: center;
        border-right: none;
    }

    form input:focus{
        outline: none;
    }

    button{
        color: #0070f3;
        border: #0070f3 solid 2px;
        border-left: none;
        border-radius: 0 5px 5px 0;
        text-decoration: none;
        font-family: monospace;
        font-size: 0.9rem;
        font-weight: bold;
        padding: 0.5rem;
        transition: 0.2s;
        background-color: white;
        width: 40px;
        box-sizing: content-box;
    }

    button:hover{
        background-color: #0070f3;
        color: white;
    }

</style>