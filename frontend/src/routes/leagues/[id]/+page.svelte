<script lang="ts">
	import { goto } from '$app/navigation';
	import api from '$lib/api';
	import MatchesTable from '$lib/components/MatchesTable.svelte';
	import SelectTeamsDialog from '$lib/components/SelectTeamsDialog.svelte';
	import TextField from '$lib/components/TextField.svelte';
	import { routes } from '$lib/config/routes';
	import type { CreateLeagueRequest } from '$lib/myApi';
	import { useDialog } from '$lib/utils/use-dialog';
	import { useDynamicRoute } from '$lib/utils/use-dynamic-route';
	import { createMutation, createQuery, useQueryClient } from '@tanstack/svelte-query';
	import { writable } from 'svelte/store';

	const client = useQueryClient();

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

	const update = createMutation({
		mutationFn: (payload: CreateLeagueRequest) => api.leagues.putLeagueById($id, payload),
		onSuccess: () => {
			client.invalidateQueries(['leagues', $id]);
		}
	});

	$: deleteAction = createMutation({
		mutationFn: () => api.leagues.deleteLeagueById($id),
		onSuccess: () => {
			client.invalidateQueries(['leagues', $id]);
			goto(routes.teams());
		}
	});

	let edited: CreateLeagueRequest | undefined;

	const setEditing = () => {
		console.log(edited);
		if (!$query.data) return;
		if (edited) {
			edited = undefined;
		} else {
			edited = {
				name: $query.data.name
			};
		}
	};
</script>

{#if id}
	<div class="flex flex-row items-center justify-center gap-3 my-3">
		{#if edited}
			<TextField label="" bind:value={edited.name} />
			<button
				class="btn btn-primary btn-sm"
				on:click={() => {
					if (edited) $update.mutateAsync(edited);
					setEditing();
				}}
				>Zapisz
			</button>
		{:else}
			<h1 class="text-xl text-center my-6 font-bold">{$query.data ? $query.data.name : ''}</h1>
			<button class="btn btn-primary btn-outline btn-sm" on:click={setEditing}>Edytuj </button>
			<button class="btn btn-error btn-outline btn-sm" on:click={() => $deleteAction.mutateAsync()}
				>Usun
			</button>
		{/if}
	</div>

	<div class="collapse collapse-plus bg-base-200">
		<input type="radio" name="my-accordion-3" />
		<div class="collapse-title text-xl font-medium">Tabela Ligi</div>
		<div class="collapse-content">
			{#if $query.isLoading}
				<span class="loading loading-spinner loading-lg mx-auto" />
			{:else if $query.data}
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
							</tr>
						{/each}
					</tbody>
				</table>
				<button on:click={openDialog} class="btn btn-outline btn-primary btn-sm mx-auto"
					>Dodaj zespół</button
				>
			{/if}
		</div>
	</div>
	<div class="collapse collapse-plus bg-base-200">
		<input type="radio" name="my-accordion-3" />
		<div class="collapse-title text-xl font-medium">Mecze w lidze</div>
		<div class="collapse-content">
			<MatchesTable data={$matchesQuery.data} />
		</div>
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
