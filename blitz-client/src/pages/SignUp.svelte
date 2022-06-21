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
    <form on:submit|preventDefault={() => handleSubmit()}>
        <h2>Sign up!</h2>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" bind:value={email} placeholder="Enter email"/>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" bind:value={username} placeholder="Enter username"/>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" bind:value={password} placeholder="Enter password"/>
        <input type="password" id="confirmPassword" name="confirmPassword" bind:value={confirmPassword} placeholder="Confirm Password"/>
        <button type="submit">Sign up</button>
    </form>
</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 92vh;
        justify-content: center;
        align-items: center;
    }

    form {
        display: flex;
        flex-direction: column;
        width: 80%;
        height: 100%;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }

    form input {
        width: 100%;
        height: 40px;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 0 10px;
        font-size: 16px;
        box-shadow: 0 0 5px #ccc;
    }

    form button{
        width: calc(100% + 20px);
    }

    button{
        color: #0070f3;
        border: #0070f3 solid 2px;
        border-radius: 5px;
        text-decoration: none;
        font-family: monospace;
        font-size: 0.9rem;
        font-weight: bold;
        padding: 0.5rem;
        transition: 0.2s;
        height: 40px;
        background-color: white;
    }

    button:hover{
        background-color: #0070f3;
        color: white;
    }
</style>