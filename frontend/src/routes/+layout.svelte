<script>
	import '../app.css';
	import Header from './Header.svelte';
</script>

<svelte:head>
	<title>LaStats</title>
	<meta name="description" content="Aplikacja lastats" />
</svelte:head>


<div class="app min-h-screen bg-base-200 flex flex-col">
	
		<Header/>
		<main class="flex-1">
			<slot />
		</main>
	
		<footer>
			<p>visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to learn SvelteKit</p>
		</footer>
		
	
</div>
