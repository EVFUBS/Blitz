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
        <button class="close" on:click={() => selectedGroup = undefined}>X</button>
        <GroupPreview group={selectedGroup} />
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

    .close{
        justify-self: flex-end;
        align-self: flex-end;
        border: none;
        font-size: 2rem;
        background-color: transparent;
        cursor: pointer;
    }

    .groups {
        margin-top: 2rem;
        width: 95%;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-gap: 20px;
        justify-content: center;
    }

    @media (max-width: 768px) {
        .groups {
            grid-template-columns: 1fr 1fr;
            grid-gap: 20px;
        }
    }
    
</style>