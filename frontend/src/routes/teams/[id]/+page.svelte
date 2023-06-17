<script lang="ts">
	import { goto } from '$app/navigation';
	import { api } from '$lib/api';
	import { routes } from '$lib/config/routes';
	import { createQuery } from '@tanstack/svelte-query';
	import { onMount } from 'svelte';

	let id: number = 0;

	onMount(() => {
		const idRaw = document.location.pathname.split('/').pop() || '';

		id = parseInt(idRaw);

		if (isNaN(id)) {
			goto(routes.addLeague());
		}
	});

	$: query = createQuery({
		queryKey: ['team', id],
		queryFn: () => api.leagues.get(id),
		enabled: id !== 0
	});
</script>

{#if id}
	{#if $query.isLoading}
		<span class="loading loading-spinner loading-lg mx-auto" />
	{:else if $query.data}
		<h1 class="mx-auto text-xl text-center my-6 font-bold">Polskie orły</h1>
		<div class="max-w-2xl mx-auto">
			<div class="collapse collapse-plus bg-base-200">
				<input type="radio" name="my-accordion-3" />
				<div class="collapse-title text-xl font-medium">Gracze w zespole</div>
				<div class="collapse-content">
					<ul>
						<li>Gracz 1</li>
						<li>Gracz 2</li>
						<li>Gracz 3</li>
					</ul>
				</div>
			</div>
			<div class="collapse collapse-plus bg-base-200">
				<input type="radio" name="my-accordion-3" />
				<div class="collapse-title text-xl font-medium">Mecze w sezonie</div>
				<div class="collapse-content">
					<p>hello</p>
				</div>
			</div>
			<div class="collapse collapse-plus bg-base-200">
				<input type="radio" name="my-accordion-3" />
				<div class="collapse-title text-xl font-medium">
					Click to open this one and close others
				</div>
				<div class="collapse-content">
					<p>hello</p>
				</div>
			</div>
		</div>
	{/if}
{/if}
