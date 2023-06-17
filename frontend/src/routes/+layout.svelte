<script>
	import { browser } from '$app/environment';
	import { QueryClientProvider, QueryClient } from '@tanstack/svelte-query';
	import { SvelteToast } from '@zerodevx/svelte-toast';

	import '../app.css';
	import Header from './Header.svelte';

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

<div class="toast-container">
	<SvelteToast options={{ reversed: true }} />
</div>

<QueryClientProvider client={queryClient}>
	<div class="app min-h-screen bg-base-200 flex flex-col">
		<Header />
		<main class="flex-1">
			<slot />
		</main>

		<footer />
	</div>
</QueryClientProvider>

<style>
	.toast-container {
		--toastContainerTop: auto;
		--toastContainerRight: 2rem;
		--toastContainerBottom: 1rem;
		--toastContainerLeft: auto;
		--toastWidth: 300px;
		--toastMinHeight: 2rem;
		--toastPadding: 0 0.5rem;
		font-size: 0.875rem;
	}
</style>
