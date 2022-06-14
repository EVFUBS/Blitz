<script lang="ts">
    import {Link} from "svelte-navigator";
</script>

<nav>
    <h2><Link class='mainLink' to='/'>Blitz</Link></h2>
    <div>
        <Link class='link' to='play'>Play</Link>
        <Link class='link' to='explore'>Explore</Link>
        <Link class='link' to='create'>Create</Link>
        <Link class='link' to='signin'>Sign in</Link>
        <Link class='link' to='signup'>Sign up</Link>
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
        border-bottom: 2px solid rgb(188, 188, 188);
    }

    nav :global(.mainLink) {
        font-size: 1.5rem;
        font-weight: bold;
        text-decoration: none;
        color: black;
    }

    nav div{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
    }

    nav div :global(.link) {
        color: black;
        text-decoration: none;
    }

    nav div :global(.link:hover) {
        color: #0070f3;
    }
</style>