<script lang="ts">
    import {Link} from "svelte-navigator";
    import { loggedIn } from "../../store";
</script>

<nav>
    <h2><Link class='mainLink' to='/'>Blitz</Link></h2>
    <div>
        <Link class='link' to='play'>Play</Link>
        <Link class='link' to='explore'>Explore</Link>
        {#if $loggedIn === false}
            <Link class='link' to='signin'>Sign in</Link>
            <Link class='link' to='signup'>Sign up</Link>
        {:else if $loggedIn === true}
            <Link class='link' to='create'>Create</Link>
            <Link class='link' to='account'>Account</Link>
        {/if}
    </div>
</nav>

<style>
    nav {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        height: 3vh;
        border-bottom: 2px solid #ccc;
    }

    nav :global(.mainLink) {
        font-size: 1.5rem;
        font-weight: bold;
        text-decoration: none;
        color: black;
        font-family: monospace;
    }
    
    nav :global(.mainLink:hover){
        color: #0070f3;
    }

    nav div{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
    }

    nav div :global(.link) {
        color: #0070f3;
        border: #0070f3 solid 1px;
        border-radius: 5px;
        text-decoration: none;
        font-family: monospace;
        font-size: 0.9rem;
        font-weight: bold;
        padding: 0.5rem;
        transition: 0.2s;
    }

    nav div :global(.link:hover) {
        background-color: #0070f3;
        color: white;
    }
</style>