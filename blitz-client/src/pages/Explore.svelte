<script lang="ts">
import GroupCard from "../components/Explore/GroupCard.svelte";
import { onMount } from "svelte";
import GroupPreview from "../components/Explore/GroupPreview.svelte";

    interface groupProps {
        group_id: number | null;
        group_name: string;
        group_description: string;
        category_id: number | null;
        author: number | null;
    }

    let groups:groupProps[] = [];
    let selectedGroup:groupProps;

    const getGroups = async () => {
        const response = await fetch('/api/quiz/groups/');
        const data = await response.json();
        if(response.status === 200) {
            groups = data;
        }
    };

    onMount(async() => {
        getGroups();
    });

</script>

<main>
    {#if selectedGroup}
        <GroupPreview group={selectedGroup} />
        <button on:click={() => selectedGroup = undefined}>press</button>
    {:else}
        <div class="groups">
            {#each groups as group}
                <div on:click={() => selectedGroup = group}>
                    <GroupCard group={group}/>
                </div>
            {/each}
        </div>
    {/if}
</main>

<style>
    
    main{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    .groups {
        margin-top: 2rem;
        width: 95%;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-gap: 20px;
        justify-content: center;
    }
    
</style>