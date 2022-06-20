<script lang="ts">
    import { group, csrf, loggedIn } from '../../store'
    import { onMount } from "svelte";
    import Group from "./Group.svelte";

    let groups = [];
    let groupName= "";
    // random number between 0 and 255
    const randomColor = () => {
        return Math.floor(Math.random() * 256);
    }

    onMount(async() => {
        const response = await fetch("/api/quiz/groups/user/", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            }
        });
        const data = await response.json();
        if(response.status === 200) {
            groups = data;
            $loggedIn = true;
        }
        else {
            alert("Failed to get groups, refresh and try again");
        }
    });

    const selectGroup = (selectedGroup: any) => {
        group.update(group => group = selectedGroup);
    }

    const handleSubmit = async() => {
        const response = await fetch(`/api/quiz/groups/submit/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            },
            body: JSON.stringify({
                group_name: groupName,
                group_description: "",
            })
        });
        if(response.status === 200 || response.status === 201) {
            const data = await response.json();
            groups = [...groups, data];
            groupName = "";
        }
        else {
            alert("Failed to create group, refresh and try again");
        }
    }

    const deleteGroup = async(group) => {
        const response = await fetch(`/api/quiz/groups/${group.group_id}/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            }
        });
        if(response.status === 200 || response.status === 201 || response.status === 204) {
            groups = groups.filter(g => g.group_id !== group.group_id);
        }
        else {
            alert("Failed to delete group, refresh and try again");
        }
    }

</script>

<main>
    {#if $group.group_id != undefined}
        <Group selectedGroup={$group} />
    {:else}
        {#await groups}
            <p>getting groups</p>
        {:then groups}
            <div class="groups">
                {#each groups as group}
                    <div class="group" style="--r: {randomColor()}; --g: {randomColor()}; --b: {randomColor()};">
                        <button class="delete" on:click={() => deleteGroup(group)}>X</button>
                        <div class="group-detail" on:click={() => selectGroup(group)}>
                            <p class="group-name">{group.group_name}</p>
                        </div>
                    </div>
                {/each}
            </div>
            <form on:submit|preventDefault={() => handleSubmit()}>
                <input type="text" name="groupName" id="" placeholder="Enter group name" bind:value={groupName}>
                <input type="submit" value="create">
            </form>
        {/await}
    {/if}
</main>

<style>

    .groups{
        margin: 1rem;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-gap: 10px;
    }

    .group{
        height: 300px;
        background-color: rgb(var(--r), var(--g), var(--b));
        border-radius: 10px;
        display: grid;
        grid-template-rows: 1fr 10fr;
    }

    .group button{
        width: 8%;
        justify-self: right;
        font-size: 1.5rem;
        display: flex;
        justify-content: center;
        background-color: transparent;
        border: none;
        cursor: pointer;
        transition: 0.3s;
        color: white;
    }

    .group-detail{
        height: 100%;
    }

    .group-name{
        height: 100%;
        width: 100%;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: white;
        transition: 0.3s;
        padding: 0;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }

    .group-name:hover{
        cursor: pointer;
        text-decoration: underline;
    }

</style>