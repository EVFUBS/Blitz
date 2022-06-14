<script lang="ts">
    let username: string = "";
    let password: string = "";

    const handleSubmit = async () => {
        const response = await fetch("/api/auth/token/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });
        const data = await response.json();
        if(response.status === 200) {
            sessionStorage.setItem("token", data.token);
            username = "";
            password = "";
        }
        else {
            alert("Login failed, please try again");
        }
    }
    
    const logout = () => {
        sessionStorage.removeItem("token");
    }
</script>

<main>
    {#if sessionStorage.getItem("token")}
        <h2>You are already logged in</h2>
        <button on:click={() => logout()}>Logout</button>
    {:else}
        <h2>Sign in</h2>
        <form on:submit|preventDefault={() => handleSubmit()}>
            <label for="username">Username</label>
            <input type="text" id="username" name="username" bind:value={username}/>
            <label for="password">Password</label>
            <input type="password" id="password" name="password" bind:value={password}/>
            <button type="submit">Sign in</button>
        </form>
    {/if}
</main>

<style>

</style>