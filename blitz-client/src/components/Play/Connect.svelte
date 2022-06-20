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