<script lang="ts">
	import { goto } from '$app/navigation';
	import api from '$lib/api';
	import MatchesTable from '$lib/components/MatchesTable.svelte';
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
		queryFn: () => api.leagues.getLeagueById($id).then((res) => res.data),
		enabled: !!$id
	});

	$: matchesQuery = createQuery({
		queryKey: ['league-matches', $id],
		queryFn: () => api.leagues.getLeagueMathes($id).then((res) => res.data),
		enabled: !!$id
	});

	const addTeams = createMutation({
		mutationFn: () => api.leagues.postLeagueTeams($id, { ids: $selected }),
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
		<table class="table w-full p-2 mb-6 text-center">
			<!-- head -->
			<thead>
				<tr>
					<th>Pozycja</th>
					<th>Punkty</th>
					<th>Nazwa</th>
					<th>Wygrane</th>
					<th>Remisy</th>
					<th>Porazki</th>
				</tr>
			</thead>
			<tbody>
				{#each $query.data.teams
					.map((team) => ({ ...team, league_points: team.wins * 3 + team.draws * 1 }))
					.sort((a, b) => b.league_points - a.league_points) as team, index}
					<tr>
						<td>{index + 1}</td>
						<td>{team.league_points}</td>
						<td>
							<a class="link link-primary" href={routes.team(team.id)}>
								{team.name}
							</a>
						</td>
						<td>{team.wins}</td>
						<td>{team.draws}</td>
						<td>{team.losses}</td>

						<td class="flex flex-row gap-6 flex-wrap justify-end">
							<button class="btn btn-error btn-outline btn-sm">Usuń z ligi</button>
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
		<hr class="my-6" />

		<details class="collapse collapse-open collapse-plus max-w-2xl mx-auto shadow-xl mb-5">
			<summary class="collapse-title">Mecze w danej lidze</summary>
			<div class="collapse-content"><MatchesTable data={$matchesQuery.data} /></div>
		</details>

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
