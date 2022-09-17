<script lang="ts">
    import Button from "../components/General/Button.svelte";
import {useNavigate} from "svelte-navigator";
    import {csrf} from "../store";
    import { fly } from "svelte/transition";
    const navigate = useNavigate();


    let email: string = "";
    let password: string = "";
    let confirmPassword: string = "";
    let username: string = "";

    const handleSubmit = async () => {
        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return;
        }
        const response = await fetch("/api/auth/users/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
            },
            body: JSON.stringify({
                email: email,
                password: password,
                username: username
            })
        });
        const data = await response.json();
        if(response.status === 201) {
            navigate("/signin");
        }
        else {
            alert("Login failed, please try again");
        }
    }
</script>

<main>
    <form in:fly={{y: -100}} on:submit|preventDefault={() => handleSubmit()}>
        <h2 class="header">Sign up!</h2>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" bind:value={email} placeholder="Enter email"/>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" bind:value={username} placeholder="Enter username"/>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" bind:value={password} placeholder="Enter password"/>
        <input type="password" id="confirmPassword" name="confirmPassword" bind:value={confirmPassword} placeholder="Confirm Password"/>
        <Button on:click={() => handleSubmit()}>Sign Up</Button>
    </form>
</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 92.4vh;
        justify-content: center;
        align-items: center;
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