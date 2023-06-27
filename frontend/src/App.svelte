<script>
  import Carousel from 'svelte-carousel'
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Character from './lib/Character.svelte';
  import Checkbox from '@smui/checkbox';
  import FormField from '@smui/form-field';
  import { onMount } from 'svelte'

  let characters = []
  let packs = [
    {name: "Base Game V2", checked: true}, 
    {name: "Four Souls+ V2", checked: false}, 
    {name: "Requiem", checked: true}, 
    {name: "Requiem Warp Zone", checked: true},
    {name: "Gold Box V2", checked: false},
    {name: "Alt Art", checked: false},
    {name: "Tapeworm", checked: false},
    {name: "Retro", checked: false},
    {name: "The Unboxing of Isaac", checked: false},
    {name: "Promo", checked: false},
  ]
  $: characters_filtered = characters.filter((character) => packs.some((pack) => pack.name === character.set_group && pack.checked))

  onMount(async () => {
    const res = await fetch('https://raw.githubusercontent.com/justdodo27/4souls-character-picker/main/frontend/characters.json')
    characters = await res.json()
    
  })

  let carousel;

  function randomPick() {
    let number = Math.floor(Math.random() * characters_filtered.length)
    console.log(number)
    carousel.goTo(number, { animated: true })
  }

</script>

<main>
  <h1>Character Picker</h1>
  <div class="card">
    <div class="filters">
      <h3 style="width: 100%; margin: 0;">Core Sets:</h3>
      {#each packs as pack, i}
        <div class="highlight">
          <input type="checkbox" name="pack-{i}" bind:checked={pack.checked}>
          <label for="pack-{i}">{pack.name}</label>
        </div>
      {/each}
    </div>
    <hr>
    <h2>Total characters: {characters_filtered.length}</h2>
    {#key characters_filtered}  
      <Carousel
        bind:this={carousel}
        infinite={true}
        particlesToShow={1}
        dots={false}
        duration={5000}
      >
        {#each characters_filtered as character}
          <Character character={character}/>      
        {/each}
    </Carousel>
    {/key}
    <button style="margin-top: 30px;" on:click={randomPick}>Pick Random</button>
  </div>
</main>

<style>
  .highlight {
    transition: all 0.5s;
  }

  .highlight:hover {
    filter: drop-shadow(5px 5px 20px white);
  }

  .filters {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin: 0px 10px;
  }

  hr {
    margin: 20px 10px;
  }
</style>
