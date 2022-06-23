<script lang="ts">
    export let content = "";
</script>

{#if content}
    <button on:click>{content}</button>
{:else}
    <button on:click>
        <slot></slot>
    </button>
{/if}

<style>
    button{
        width: 100%;
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
        box-sizing: border-box;
    }

    button:hover{
        background-color: #0070f3;
        color: white;
    }
</style>