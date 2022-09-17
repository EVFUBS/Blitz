<script lang="ts">
    import { Link } from 'svelte-navigator'
    import { loggedIn } from "../../store";
    import { fly } from 'svelte/transition';
    import Fa from 'svelte-fa'
    import {faBars, faXmark} from '@fortawesome/free-solid-svg-icons'
    
    let menu: HTMLDivElement;
    let width: number;
    let open = false;

    $: if(width < 768) {
        open = false;
    }

    $: if(width > 768) {
        open = true;
    }

    const toggleMenu = () => {
        if(open) {
            open = false;
        }
        else {
            open = true;
        }
        console.log(open);
    };

    const closeMenu = () => {
        if(width < 768) {
            open = false;
        }
    };

</script>

<svelte:window bind:innerWidth={width} />

<nav>
    <h2><Link class='mainLink' to='/'>BLITZ</Link></h2>
    <div class="open" on:click={toggleMenu}><Fa icon={faBars}/></div>
    {#if open}
        <div class="links" in:fly={{x: 100,}} out:fly={{x: 100}}>
            <div class="close" on:click={toggleMenu}><Fa icon={faXmark}/></div>
            <Link class='link' to='play' on:click={() => closeMenu()}>Play</Link>
            <Link class='link' to='explore' on:click={() => closeMenu()}>Explore</Link>
            {#if $loggedIn === false}
                <Link class='link' to='signin' on:click={() => closeMenu()}>Sign in</Link>
                <Link class='link' to='signup' on:click={() => closeMenu()}>Sign up</Link>
            {:else if $loggedIn === true}
                <Link class='link' to='create' on:click={() => closeMenu()}>Create</Link>
                <Link class='link' to='account' on:click={() => closeMenu()}>Account</Link>
            {/if}
            <Link class='link' to='settings' on:click={() => closeMenu()}>Settings</Link>
        </div>
    {/if}
</nav>

<style>
    nav {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        height: 3vh;
        background-color: var(--theme-color);
        border-bottom: 2px solid var(--theme-color-2);
    }

    nav :global(.mainLink) {
        font-size: 1.5rem;
        font-weight: bold;
        text-decoration: none;
        color: var(--theme-color-2);
        font-family: monospace;
    }
    
    nav :global(.mainLink:hover){
        color: var(--theme-color-alt);
    }

    nav div{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
    }

    nav div :global(.link) {
        color: var(--theme-color-alt);
        border: var(--theme-color-alt) solid 1px;
        border-radius: 5px;
        text-decoration: none;
        font-family: monospace;
        font-size: 0.9rem;
        font-weight: bold;
        padding: 0.5rem;
        transition: 0.2s;
    }

    nav div :global(.link:hover) {
        background-color: var(--theme-color-alt);
        color: var(--theme-color);
    }

    .open{
        display: none;
        color: var(--theme-color-2);
    }

    .close{
        display: none;
        color: var(--theme-color-2);
    }

    @media (max-width: 768px) {
        .open{
            display: block;
            cursor: pointer;
            width: 30px;
            font-size: 2rem;
        }

        .open:hover {
            color: var(--theme-color-alt);
        }

        .close{
            display: block;
            cursor: pointer;
            position: fixed;
            top: 3%;
            left: 88%;
            width: 30px;
            font-size: 3rem;
        }

        .close:hover {
            color: var(--theme-color-alt);
        }

        .links{
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            background-color: var(--theme-color);
            z-index: 10;
        }

        nav div :global(.link){
            width: 25%;
            text-align: center;
        }
    }
</style>