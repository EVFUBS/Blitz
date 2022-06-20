<script lang="ts">
    interface groupProps {
        group_id: number;
        group_name: string;
        group_description: string;
        category_id: number | null;
        author: number | null;
    }

    export let group: groupProps;

    const genRGBColor = () => {
        const r = Math.floor(Math.random() * 256);
        const g = Math.floor(Math.random() * 256);
        const b = Math.floor(Math.random() * 256);
        return `rgb(${r}, ${g}, ${b})`;
    };
</script>

<main>
    <div class="title-wrapper" style="background-color: {genRGBColor()};">
        <p class="title">{group.group_name}</p>
    </div>
    <div class="desc-wrapper">
        <p class="desc">{group.group_description}</p>
    </div>
</main>

<style>

    main{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        border: 1px black solid;
        border-radius: 10px;
        cursor: pointer;
    }

    main:hover{
        background-color: #f5f5f5;
    }

    main:active{
        background-color: #e4e4e4;
    }

    .title-wrapper{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        border-bottom: 1px black solid;
        border-radius: 10px 10px 0 0;
    }

    .title{
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
        color: white;
    }

    .desc-wrapper{
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        height: 120px;
        text-align: center;
    }

</style>