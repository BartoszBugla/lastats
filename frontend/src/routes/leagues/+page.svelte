<script lang="ts">
	import api from '$lib/api';
	import TextField from '$lib/components/TextField.svelte';
	import { routes } from '$lib/config/routes';
	import type { CreateLeagueRequest, LeagueModel } from '$lib/myApi';
	import { createMutation, createQuery, useQueryClient } from '@tanstack/svelte-query';
	import { bind } from 'svelte/internal';

	let searchValue = '';

	const client = useQueryClient();

	const query = createQuery({
		queryKey: ['leagues'],
		queryFn: async () => await api.leagues.getLeagues().then((res) => res.data)
	});

	$: data = $query.data?.filter((league) => league.name.includes(searchValue)) || [];

	const deleteAction = createMutation({
		mutationFn: (id: number) => api.leagues.deleteLeagueById(id),
		onSuccess: () => {
			client.invalidateQueries(['leagues']);
		}
	});

	let edited: (CreateLeagueRequest & { id: number }) | undefined;

	const setEdited = (league?: LeagueModel) => {
		if (!league) {
			edited = undefined;
		} else {
			edited = {
				id: league.id,
				name: league.name
			};
		}
	};

	const updateAction = createMutation({
		mutationFn: ({ id, ...edited }: CreateLeagueRequest & { id: number }) =>
			api.leagues.putLeagueById(id, edited),
		onSuccess: () => {
			client.invalidateQueries(['leagues']);
		}
	});
</script>

<section class="flex flex-col">
	<div>
		<div class="flex flex-row gap-3 items-end justify-center">
			<TextField label="Szukaj po nazwie" bind:value={searchValue} />
		</div>

		<div class="overflow-x-auto mx-auto w-auto px-6 max-w-2xl">
			<table class="table w-full p-2 mb-6">
				<!-- head -->
				<thead>
					<tr>
						<th>Nazwa</th>
						<th />
					</tr>
				</thead>
				<tbody>
					{#if $query.isLoading}
						<span class="loading loading-spinner loading-lg mx-auto" />
					{:else if $query.isSuccess}
						{#each data as league}
							{#if edited && league.id === edited.id}
								<tr>
									<td> <TextField label="" bind:value={edited.name} /></td>

									<td class="flex flex-row gap-6 flex-wrap justify-end">
										<button
											class="btn btn-primary btn-sm"
											on:click={() => {
												edited && $updateAction.mutateAsync(edited);
												setEdited();
											}}>Zapisz</button
										>
									</td>
								</tr>
							{:else}
								<tr>
									<td>
										<a href={routes.league(league.id)} class="link link-secondary">
											{league.name}
										</a>
									</td>

									<td class="flex flex-row gap-6 flex-wrap justify-end">
										<button class="btn btn-primary btn-sm" on:click={() => setEdited(league)}
											>Edytuj</button
										>
										<button
											class="btn btn-error btn-outline btn-sm"
											on:click={() => $deleteAction.mutateAsync(league.id)}>Delete</button
										>
									</td>
								</tr>
							{/if}
						{/each}
					{/if}
				</tbody>
			</table>
		</div>
	</div>
</section>
