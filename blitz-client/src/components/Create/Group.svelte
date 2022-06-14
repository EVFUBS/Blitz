<script lang="ts">
import { group } from '../../store'
import Questions from './Questions.svelte'

    interface groupProps {
        group_id: number 
        group_name: string
        group_description: string
        category_id: number
        author: number
    }

    export let selectedGroup: groupProps

    const unSelectGroup = () => {
        group.update(group => group = {
            group_id: undefined,
            group_name: undefined,
            group_description: undefined,
            category_id: undefined,
            author: undefined
        })
    }

    const updateGroup = async() => {
        const response = await fetch(`/api/quiz/groups/${selectedGroup.group_id}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Token " + sessionStorage.getItem("token")
            },
            body: JSON.stringify(selectedGroup)
        });
        const data = await response.json();
        if(response.status === 200) {
            selectedGroup = data;
        }
        else {
            alert("Failed to update group, refresh and try again");
        }
    }

</script>

<main>
    <h2>Group</h2>
    <form on:submit|preventDefault={() => updateGroup()}>
        <input type="text" bind:value={selectedGroup.group_name}>
        <input type="text" bind:value={selectedGroup.group_description}>
        <p>Category: {selectedGroup.category_id}</p>
        <p>Author: {selectedGroup.author}</p>
        <input type="submit" value="submit">
    </form>
    <Questions group_id={selectedGroup.group_id} />
    <button on:click={() => unSelectGroup()}>close group</button>
</main>

<style>

</style>