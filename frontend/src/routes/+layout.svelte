<script>
	export const prerender = true;

	import '../app.css';
	import Header from './Header.svelte';

	import { browser } from '$app/environment';
	import { QueryClientProvider, QueryClient } from '@tanstack/svelte-query';

	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				enabled: browser
			}
		}
	});
</script>

<svelte:head>
	<title>LaStats</title>
	<meta name="description" content="Aplikacja lastats" />
</svelte:head>

<QueryClientProvider client={queryClient}>
	<div class="app min-h-screen bg-base-200 flex flex-col">
		<Header />
		<main class="flex-1">
			<slot />
		</main>

		<footer>
			<p>visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to learn SvelteKit</p>
		</footer>
	</div>
</QueryClientProvider>
