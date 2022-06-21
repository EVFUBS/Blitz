<script lang="ts">
import { onMount } from "svelte";

import { navigate } from "svelte-navigator";
import { loggedIn, csrf } from "../store";

    interface userProps{
        id: number | null;
        username: string;
        email: string;
        password: string | undefined;
        date_joined: string;
        last_login: string;
    }

    let user: userProps;
    let confirmPassword: string | undefined;

    const logout = async() => {
        const response = await fetch('/api/auth/logout/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
                'CSRF-Token': $csrf
            }
        });
        const data = await response.json();
        if(response.status === 200 || response.status === 201) {
            $loggedIn = false;
            navigate("/signin");
        }
        else {
            alert("Logout failed, please try again");
        }
    }

    const getCurrentUser = async() => {
        const response = await fetch('/api/auth/currentUser/', {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
                'CSRF-Token': $csrf
            }
        });
        const data = await response.json();
        if(response.status === 200 || response.status === 201) {
            user = data;
        }
        else {
            alert("Failed to get user data, please try again");
        }
    }

    const updateUser = async() => {
        if(user.password !== confirmPassword) {
            alert("Passwords do not match");
        }
        else if (user.password === undefined && confirmPassword === undefined){
            alert("Please enter a password");
        }
        else{
            const response = await fetch(`/api/auth/users/${user.id}/`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": $csrf,
                    'CSRF-Token': $csrf
                },
                body: JSON.stringify({
                    username: user.username,
                    email: user.email,
                    password: user.password
                })
            });
            if(response.status === 200 || response.status === 201) {
                alert("User updated successfully");
            }
            else {
                alert("Failed to update user, please try again");
            }
        }
    }
</script>

<main>
    {#await getCurrentUser()}
        <p>getting user</p>
    {:then} 
        <div class="account">
            <form on:submit|preventDefault={() => updateUser()}>
                <label for="username">Username</label>
                <input type="text" name="username" bind:value={user.username} placeholder="Enter username">
                <label for="email">Email</label>
                <input type="text" name="email" bind:value={user.email} placeholder="Enter email">
                <label for="password">Password</label>
                <input type="password" name="password" bind:value={user.password} placeholder="Enter password">
                <input type="password" name="confirmPassword" bind:value={confirmPassword} placeholder="Confirm password">
                <button type="submit">Update Info</button>
            </form>
            <button on:click={() => logout()}>logout</button>
        </div>
    {/await}
</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 92vh;
        width: 100%;
    }

    .account{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        height: 100%;
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
        border: #0070f3 solid 1px;
        border-radius: 5px;
        text-decoration: none;
        font-family: monospace;
        font-size: 0.9rem;
        font-weight: bold;
        padding: 0.5rem;
        transition: 0.2s;
        background-color: white;
        width: 82%;
        height: 40px;
    }

    button:hover{
        background-color: #0070f3;
        color: white;
    }


</style>