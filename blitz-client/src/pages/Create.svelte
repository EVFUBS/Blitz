<script lang="ts">
    import { navigate } from "svelte-navigator";
    import Groups from "../components/Create/Groups.svelte";
    import {loggedIn} from '../store'
    if (!$loggedIn) {
        navigate('/signup')
    }

</script>

<main>
    <Groups />
</main>

<style>

    main{
        width: 100%;
        background-color: var(--theme-color);
    }
    
</style>