<script lang="ts">
import { onMount } from "svelte";

    import Connect from "../components/Play/Connect.svelte";

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
        <p>Enter Room Code</p>
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
    }

    form{
        display: flex;
        flex-direction: row;
        justify-content: center;
        width: 100%;
        height: 20%;
    }

    form input{
        width: 300px;
        margin-bottom: 10px;
        height: 51px;
        border-radius: 5px 0 0 5px;
        border: 1px solid #ccc;
        font-size: larger;
        text-align: center;
        border-right: none;
    }

    form input:focus{
        outline: none;
    }

    form button{
        height: 54px;
        width: 50px;
        border-radius: 0 5px 5px 0;
        border: 1px solid #ccc;
        border-left: none;
        font-size: larger;
        color: white;
        background-color: black;
    }

    form button:focus{
        outline: none;
    }
    
</style>