<script lang="ts">
    import {useNavigate} from "svelte-navigator";
    import {csrf} from "../store";
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
    <h2>Sign up!</h2>
    <form on:submit|preventDefault={() => handleSubmit()}>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" bind:value={email}/>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" bind:value={username}/>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" bind:value={password}/>
        <label for="confirmPassword">Confirm Password</label>
        <input type="password" id="confirmPassword" name="confirmPassword" bind:value={confirmPassword}/>
        <button type="submit">Sign up</button>
    </form>
</main>

<style>
    main form{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>