<script lang="ts">
import Button from "../components/General/Button.svelte";
import { navigate } from "svelte-navigator";
import { loggedIn } from "../store";

</script>

<main>
    <div>
        <h1>Welcome to <span>BLITZ</span></h1>
        <p>
            BLITZ is a game where you can play quizes against other players and compete
            for highscores
        </p>
        <strong>
            <Button on:click={() => navigate('/play')}>Play</Button>
        </strong>
    </div>
    <div>
        <h2><span>Explore</span> offical and usermade quizes</h2>
        <p>
            Explore quizes created by other users or by the offical BLITZ team.
        </p>
        <strong>
            <Button on:click={() => navigate('/explore')}>Explore</Button>
        </strong>
    </div>
    <div>
        <h2><span>Create</span> your own quizes</h2>
        <p>
            Play quizes made by other users, or create your own!
            Just create an account and make the quiz you always wanted to make!
        </p>
        <strong>
            {#if $loggedIn === false}
                <Button on:click={() => navigate('/signin')}>Sign in</Button>
            {:else if $loggedIn === true}
                <Button on:click={() => navigate('/create')}>Create</Button>
            {/if}
        </strong>
    </div>
    <div>
        <h2>Compete for <span>highscores</span></h2>
        <p>
            Compete for bragging rights and for a place on the global leaderboard.
            Make sure to sign in to compete for highscores!
        </p>
    </div>
</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    span{
        color: #0070f3;
    }

    div{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 90vh;
        width: 100%;
        text-align: center;
    }

    strong{
        width: 55%;
    }

    h1{
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    h1:focus{
        outline: none;
    }

    h2{
        font-size: 1.7rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }

    p{
        font-size: 1.2rem;
        width: 60%;
    }

    @media (max-width: 768px) {
        h1{
            font-size: 2.2rem;
        }

        h2{
            font-size: 1.5rem;
        }

        p{
            font-size: 1rem;
            width: 90%;
        }
    }

</style>