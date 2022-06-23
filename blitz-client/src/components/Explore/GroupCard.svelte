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
        height: 200px;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0px 0px 3px 0px rgba(0,0,0,0.75);
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
        justify-content: center;
        text-align: center;
        width: 100%;
        height: 50px;
        border-radius: 10px 10px 0 0;
        overflow: hidden;
    }

    @media (max-width: 768px) {
        .title-wrapper{
            height: 60px;
        }
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
        height: 120px;
        text-align: center;
        border-radius: 0 0 10px 10px;
        overflow: hidden;
    }

</style>