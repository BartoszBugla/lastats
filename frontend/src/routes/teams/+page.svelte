<script lang="ts">
	import api from '$lib/api';
	import TextField from '$lib/components/TextField.svelte';
	import { routes } from '$lib/config/routes';
	import type { CreateTeamRequest, TeamModel } from '$lib/myApi';
	import { createMutation, createQuery, useQueryClient } from '@tanstack/svelte-query';

	let searchValue = '';

	const client = useQueryClient();

	const query = createQuery({
		queryKey: ['teams'],
		queryFn: async () => await api.teams.getTeams().then((res) => res.data)
	});

	$: data = $query.data?.filter((team) => team.name.includes(searchValue)) || [];

	const deleteAction = createMutation({
		mutationFn: (id: number) => api.teams.deleteTeamById(id),
		onSuccess: () => {
			client.invalidateQueries(['teams']);
		}
	});

	let edited: (CreateTeamRequest & { id: number }) | undefined;

	const setEdited = (team?: TeamModel) => {
		if (!team) {
			edited = undefined;
		} else {
			edited = {
				id: team.id,
				name: team.name
			};
		}
	};

	const updateAction = createMutation({
		mutationFn: ({ id, ...edited }: CreateTeamRequest & { id: number }) =>
			api.teams.putTeamById(id, edited),
		onSuccess: () => {
			client.invalidateQueries(['teams']);
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
						{#each data as team}
							{#if edited && team.id === edited.id}
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
										<a href={routes.team(team.id)} class="link link-primary">
											{team.name}
										</a>
									</td>

									<td class="flex flex-row gap-6 flex-wrap justify-end">
										<button class="btn btn-primary btn-sm" on:click={() => setEdited(team)}
											>Edytuj</button
										>
										<button
											class="btn btn-error btn-outline btn-sm"
											on:click={() => $deleteAction.mutateAsync(team.id)}>Delete</button
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
