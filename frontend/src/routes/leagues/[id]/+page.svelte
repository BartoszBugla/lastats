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
		queryKey: ['leagues', id],
		queryFn: () => api.leagues.get(id),
		enabled: id !== 0
	});
</script>

{#if id}
	{#if $query.isLoading}
		<span class="loading loading-spinner loading-lg mx-auto" />
	{:else if $query.data}
		<h1 class="mx-auto text-xl text-center my-6">{$query.data.name}</h1>
		<table class="table w-full p-2 mb-6">
			<!-- head -->
			<thead>
				<tr>
					<th />
					<th>id</th>
					<th>Name</th>
					<th />
				</tr>
			</thead>
			<tbody>
				{#each $query.data.teams as team}
					<tr>
						<td />
						<td>{team.id}</td>
						<td>{team.name}</td>

						<td class="flex flex-row gap-6 flex-wrap justify-end">
							<a class="btn btn-primary btn-sm" href={routes.league(team.id)}>Zobacz</a>
							<button class="btn btn-error btn-outline btn-sm">Delete</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{/if}
{/if}
