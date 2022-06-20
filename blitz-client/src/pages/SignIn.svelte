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
    <h2>Sign in</h2>
    <form on:submit|preventDefault={() => handleSubmit()}>
        <label for="username">Username</label>
        <input type="text" id="username" name="username" bind:value={username}/>
        <label for="password">Password</label>
        <input type="password" id="password" name="password" bind:value={password}/>
        <button type="submit">Sign in</button>
    </form>
</main>

<style>

</style>