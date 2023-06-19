<script lang="ts">
	import { goto } from '$app/navigation';
	import api from '$lib/api';
	import SelectTeamsDialog from '$lib/components/SelectTeamsDialog.svelte';
	import { routes } from '$lib/config/routes';
	import { useDialog } from '$lib/utils/use-dialog';
	import { useDynamicRoute } from '$lib/utils/use-dynamic-route';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { writable } from 'svelte/store';

	let selected = writable<number[]>([]);

	const cleanSelected = () => selected.set([]);

	let id = useDynamicRoute<number>({
		isNumeric: true,
		fallbackAction: () => goto(routes.leagues())
	});

	const [isOpenDialog, openDialog, closeDialog] = useDialog();

	$: query = createQuery({
		queryKey: ['leagues', $id],
		queryFn: () => api.teams.getTeam($id),
		enabled: !!$id
	});

	const addTeams = createMutation({
		mutationFn: () => api.teams.postTeam($id, { ids: $selected }),
		onError: () => {
			cleanSelected();
			closeDialog();
		},
		onSuccess: () => {
			cleanSelected();
			closeDialog();
			$query.refetch();
		}
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
					<th>Points</th>
					<th>Name</th>
					<th>Wins</th>
					<th>Draws</th>
					<th>Losses</th>
					<th>Balance</th>
				</tr>
			</thead>
			<tbody>
				{#each $query.data.teams as team}
					<tr>
						<td />
						<td>{team.id}</td>
						<td>12</td>
						<td>{team.name}</td>
						<td>2</td>
						<td>3</td>
						<td>2</td>
						<td>32:21</td>
						<td class="flex flex-row gap-6 flex-wrap justify-end">
							<a class="btn btn-primary btn-sm" href={routes.team(team.id)}>Zobacz</a>
							<button class="btn btn-error btn-outline btn-sm">Delete</button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
		<div class="w-full flex justify-center">
			<button class="btn btn-primary btn-sm mx-auto btn-outline" on:click={openDialog}
				>Dodaj zespół</button
			>
		</div>

		<SelectTeamsDialog
			leagueId={$id}
			onCancel={cleanSelected}
			isOpened={$isOpenDialog}
			onSubmit={$addTeams.mutateAsync}
			{closeDialog}
			bind:selected={$selected}
		/>
	{/if}
{/if}
