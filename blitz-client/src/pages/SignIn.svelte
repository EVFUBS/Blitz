<script lang="ts">
    import {csrf, loggedIn} from "../store";
    let username: string = "";
    let password: string = "";
    import {useNavigate} from "svelte-navigator";
    import Button from "../components/General/Button.svelte";
    import { fly } from "svelte/transition";
    const navigate = useNavigate();

    const handleSubmit = async () => {
        const response = await fetch("/api/auth/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });
        const data = await response.json();
        if(response.status === 200 || response.status === 201) {
            const newcsrf = await fetch("/api/auth/csrf/", {
                method: "GET",
                headers: {
                "Content-Type": "application/json"
                }
            });
            const csrfData = await newcsrf.json();
            $csrf = csrfData.csrf_token;
            username = "";
            password = "";
            $loggedIn = true;
            navigate("/account");
        }
        else {
            alert("Login failed, please try again");
        }
    }
</script>

<main>
    <form in:fly={{y: -100}} on:submit|preventDefault={() => handleSubmit()}>
        <h2 class="header">Sign in</h2>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" bind:value={username}/>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" bind:value={password}/>
        <Button on:click={() => handleSubmit()}>Sign in</Button>
    </form>
</main>

<style>
    main{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 92.4vh;
        background-color: var(--theme-color);
    }

    .header {
        color: var(--theme-color-2);
    }

    label {
        color: var(--theme-color-2);
    }

    form {
        display: flex;
        flex-direction: column;
        width: 70%;
        height: 100%;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }

    form input {
        width: 99%;
        height: 40px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        box-shadow: 0 0 5px #ccc;
    }
</style>