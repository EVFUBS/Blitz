<script lang="ts">
import { onMount } from "svelte";

import { navigate } from "svelte-navigator";
import { loggedIn, csrf } from "../store";

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

    onMount(async() => {
        const response = await fetch('/api/auth/currentUser/', {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf,
                'CSRF-Token': $csrf
            }
        });
    })
</script>

<main>
    <h2>account</h2>
    <button on:click={() => logout()}>logout</button>
</main>

<style>

</style>