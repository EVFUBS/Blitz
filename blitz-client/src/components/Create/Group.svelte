<script lang="ts">
import { group } from '../../store'
import Questions from './Questions.svelte'
import {csrf} from '../../store'
import Button from '../General/Button.svelte'
import {onMount} from 'svelte'

    interface groupProps {
        group_id: number 
        group_name: string
        group_description: string
        category_id: number
        author: number
    }

    interface author{
        id: number | null
        username: string
        email: string
        date_joined: string
        last_login: string
    }

    export let selectedGroup: groupProps;
    let author: author;
    let submitted: boolean = false;

    onMount(async() => {
        const response = await fetch(`/api/auth/users/${selectedGroup.author}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": $csrf
            }
        });
        const data = await response.json();
        author = data;
    });

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
                "X-CSRFToken": $csrf
            },
            body: JSON.stringify(selectedGroup)
        });
        const data = await response.json();
        if(response.status === 200) {
            selectedGroup = data;
            submitted = true;
            setTimeout(() => {
                submitted = false;
            }, 5000);
        }
        else {
            alert("Failed to update group, refresh and try again");
        }
    }

</script>

<main>
    <h2>{selectedGroup.group_name}</h2>
    <form on:submit|preventDefault={() => updateGroup()}>
        <label for="title">Title:</label>
        <input class="title" name="title" type="text" placeholder="Enter Group Name" bind:value={selectedGroup.group_name}>
        <label for="desc">Description:</label>
        <textarea class="desc" type="text" name="desc" placeholder="Enter Description" bind:value={selectedGroup.group_description}/>
        <p>Category: {selectedGroup.category_id}</p>
        {#if author !== undefined}
            <p>Author: {author.username}</p>
        {:else}
            <p>Author: unknown</p>
        {/if}
        {#if submitted === false}
            <Button>Update Info</Button>
        {:else}
            <div class="submit"><div class="lds-ring"><div></div><div></div><div></div><div></div></div></div>
        {/if}
    </form>
    <Questions group_id={selectedGroup.group_id} unSelectGroup={unSelectGroup}/>
    <div style="width: 80%; margin-bottom: 2rem;">
        <Button on:click={() => unSelectGroup()}>Close</Button>
    </div>
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    h2{
        text-align: center;
    }

    form{
        display: flex;
        flex-direction: column;
        width: 80%;
    }

    form *{
        margin-bottom: 0.5rem;
    }

    form .title{
        border: none;
        border-bottom: 1px solid black;
        font-size: large;
        padding: 0.5rem;
    }

    form .title:focus{
        outline: none
    }

    form .desc{
        border: none;
        border-bottom: 1px solid black;
        font-size: large;
        height: 10rem;
        width: 100%;
        resize: none;
        padding: 0.5rem;
    }

    form .desc:focus{
        outline: none
    }

    .submit{
        color: rgb(0, 243, 12);
        border-radius: 5px;
        text-decoration: none;
        font-family: monospace;
        font-size: 0.9rem;
        font-weight: bold;
        padding: 0.5rem;
        transition: 0.2s;
        background-color: rgb(0, 243, 12);
        height: 40px;
        box-sizing: border-box;
        width: 100%;
        height: 40px;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .lds-ring {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 80px;
    top: 20px;
    left: 20px;
    }
    .lds-ring div {
    box-sizing: border-box;
    display: block;
    position: absolute;
    width: 32px;
    height: 32px;
    margin: 8px;
    border: 8px solid #fff;
    border-radius: 50%;
    animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    border-color: #fff transparent transparent transparent;
    }
    .lds-ring div:nth-child(1) {
    animation-delay: -0.45s;
    }
    .lds-ring div:nth-child(2) {
    animation-delay: -0.3s;
    }
    .lds-ring div:nth-child(3) {
    animation-delay: -0.15s;
    }
    @keyframes lds-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
    }


</style>