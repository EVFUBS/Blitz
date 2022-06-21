<script lang="ts">
    import {csrf, loggedIn} from "../store";
    let username: string = "";
    let password: string = "";
    import {useNavigate} from "svelte-navigator";
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
    <form on:submit|preventDefault={() => handleSubmit()}>
        <h2>Sign in</h2>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" bind:value={username}/>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" bind:value={password}/>
        <button type="submit">Sign in</button>
    </form>
</main>

<style>
    main{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 92vh;
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
        background-color: white;
        height: 40px;
    }

    button:hover{
        background-color: #0070f3;
        color: white;
    }

</style>