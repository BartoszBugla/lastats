<script lang="ts">
	import { goto } from '$app/navigation';
	import api from '$lib/api';
	import TextField from '$lib/components/TextField.svelte';
	import { routes } from '$lib/config/routes';
	import type { CreateTeamRequest, TeamModel } from '$lib/myApi';
	import { createMutation, createQuery, useQueryClient } from '@tanstack/svelte-query';
	import { onMount } from 'svelte';
	import { each } from 'svelte/internal';

	const client = useQueryClient();

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
		queryFn: () => api.teams.getTeamById(id).then((res) => res.data),
		enabled: id !== 0
	});

	$: deleteAction = createMutation({
		mutationFn: () => api.teams.deleteTeamById(id),
		onSuccess: () => {
			client.invalidateQueries(['team', id]);
			goto(routes.teams());
		}
	});

	$: update = createMutation({
		mutationFn: (payload: CreateTeamRequest) => api.teams.putTeamById(id, payload),
		onSuccess: () => {
			client.invalidateQueries(['team', id]);
		}
	});

	let edited: CreateTeamRequest | undefined;

	const setEditing = () => {
		if (!$query.data) return;
		if (edited) {
			edited = undefined;
		} else {
			edited = {
				name: $query.data.name
			};
		}
	};

	const translatePositon = (pos: string) => {
		if (pos === 'PlayerPosition.GOALKEEPER') return 'Bramkarz';
		if (pos === 'PlayerPosition.DEFENDER') return 'Obronca';
		if (pos === 'PlayerPosition.MIDFIELDER') return 'Pomocnik';
		if (pos === 'PlayerPosition.FORWARD') return 'Napastnik';
		return 'Brak';
	};
</script>

{#if id}
	{#if $query.isLoading}
		<span class="loading loading-spinner loading-lg mx-auto" />
	{:else if $query.data}
		<div class="flex flex-row items-center justify-center gap-3 my-3">
			{#if edited}
				<TextField label="" bind:value={edited.name} />
				<button
					class="btn btn-primary btn-sm"
					on:click={() => {
						edited && $update.mutateAsync(edited);
						setEditing();
					}}
					>Zapisz
				</button>
			{:else}
				<h1 class="text-xl text-center my-6 font-bold">{$query.data.name}</h1>
				<button class="btn btn-primary btn-outline btn-sm" on:click={setEditing}>Edytuj </button>
				<button
					class="btn btn-error btn-outline btn-sm"
					on:click={() => $deleteAction.mutateAsync()}
					>Usun
				</button>
			{/if}
		</div>

		<div class="max-w-2xl mx-auto">
			<div class="collapse collapse-plus bg-base-200">
				<input type="radio" name="my-accordion-3" />
				<div class="collapse-title text-xl font-medium">Gracze w zespole</div>
				<div class="collapse-content">
					<table class="table table-sm w-full p-2 mb-6">
						<thead>
							<tr class="border-b border-gray-600">
								<th>Numer na koszulce</th>
								<th>Zawodnik</th>
								<th>Pozycja</th>
							</tr>
						</thead>
						<tbody>
							{#each $query.data.players as player}
								<tr>
									<td>{player.number}</td>
									<td>{player.name}</td>
									<td>{translatePositon(player.position)}</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</div>
			</div>
		</div>
	{/if}
{/if}
