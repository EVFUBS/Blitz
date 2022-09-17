<script lang="ts">
    import { theme, themeColor, themeColor2, themeColorAlt } from "../store";
    import Switch from "../components/General/Switch.svelte";

    const flipTheme = () => {
        if ($theme) {
            $themeColor = '#1B2430'
            $themeColor2 = 'white'
            $themeColorAlt = '#ECDBBA'
        } else {
            $themeColor = 'white'
            $themeColor2 = 'black'
            $themeColorAlt = '#0070f3'
        }
        document.documentElement.style.setProperty('--theme-color', $themeColor)
        document.documentElement.style.setProperty('--theme-color-2', $themeColor2)
        document.documentElement.style.setProperty('--theme-color-alt', $themeColorAlt)
        $theme = !$theme
    }

    
</script>

<div class="settings">
    <h2 class="settings-header">Settings</h2>
    <div class="settings-body">
        <div class="setting">
            <p>Dark mode:</p>
            <Switch val={$theme} on:click={() => flipTheme()}/>
        </div>
    </div>


</div>

<style>
    .settings {
        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: var(--theme-color);
    }

    .settings-header {
        padding: 0.2rem;
        color: var(--theme-color-2);
    }

    .settings-body {
        display: flex;
        flex-direction: column;
        width: 100%;
    }

    .setting {
        display: flex;
        flex-direction: row;
        justify-content:space-evenly;
        align-items: center;
        color: var(--theme-color-2);
    }
</style>