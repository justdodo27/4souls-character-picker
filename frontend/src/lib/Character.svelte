<script>
    export let character;

    $: bgImage = `background-image: url("${character.image_url}");`;
</script>

<div>
    <div class="layout">
        <div class="details" style="{bgImage}">
            
        </div>
    </div>
</div>

<style>
    .layout {
        width: 100%;
        display: flex;
        justify-content: center;
        padding: 20px 0px;
    }

    .details:hover {
        transform: rotateX(10deg) rotateY(10deg);
    }

    div.details {
        transition: all 0.4s;
        height: 320px;
        width: 200px;
        border-radius: 20px;
        padding: 20px;
        background-position: center;
        background-size: cover;
        position: relative;
    }

    div.name {
        background-color: antiquewhite;
        width: 100%;
        color: black;
        text-transform: uppercase;
        border: 2px solid black;
        border-radius: 5px;
        position: absolute;
        bottom: 10px;
        left: 0px;
    }
</style>