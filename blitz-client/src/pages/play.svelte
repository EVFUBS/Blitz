<script lang="ts">
import { onMount } from "svelte";

    import Connect from "../components/Play/Connect.svelte";
    import {fly} from "svelte/transition"

    let code: string;
    let codeEntered: boolean = false;

    onMount(() => {
        window.scrollTo(0, document.body.scrollHeight);
    })
    
</script>

<main>
    {#if codeEntered}
        <Connect code={code}/>
    {:else}
        <h3>Enter Room Code</h3>
        <form on:submit|preventDefault>
            <input type="text" bind:value={code}>
            <button type="submit" on:click={() => codeEntered = true}>></button>
        </form>
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
        background-color: var(--theme-color);
    }

    h3 {
        color: var(--theme-color-2);
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
        border: 2px solid var(--theme-color-alt);
        font-size: larger;
        text-align: center;
        border-right: none;
    }

    form input:focus{
        outline: none;
    }

    button{
        color: var(--theme-color-alt);
        border: var(--theme-color-alt) solid 2px;
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
        background-color: var(--theme-color-alt);
        color: var(--theme-color);
    }
    
</style>