<script lang="ts">
	import { goto } from '$app/navigation';
	import { api } from '$lib/api';
	import { routes } from '$lib/config/routes';
	import { createQuery } from '@tanstack/svelte-query';
	import { onMount } from 'svelte';

	let id: number = 0;
	let isDialogOpened = false;

	let openDialog = () => {
		isDialogOpened = true;
	};

	let closeDialog = () => {
		isDialogOpened = false;
	};

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
				<tr>
					<td />
					<td />
					<td />
					<td />
					<td />
					<td />
					<td />
					<td />
					<td class="flex flex-row gap-6 flex-wrap justify-end">
						<button class="btn btn-primary btn-sm" on:click={openDialog}>Dodaj zespół</button>
					</td>
				</tr>
			</tbody>
		</table>
	{/if}
	<dialog class="modal" open={isDialogOpened} on:close={closeDialog}>
		<form method="dialog" class="modal-box">
			<h3 class="font-bold text-lg h-1/2">Hello!</h3>
			<p class="py-4">Press ESC key or click the button below to close</p>
			<div class="modal-action flex flex-col">
				<table class="table w-full p-2 mb-6">
					<!-- head -->
					<thead>
						<tr>
							<th />
							<th>id</th>
							<th>Points</th>
							<th>Name</th>
						</tr>
					</thead>
					<tbody>
						{#each $query.data.teams as team}
							<tr>
								<th>
									<label>
										<input type="checkbox" class="checkbox" />
									</label>
								</th>
								<td>{team.id}</td>
								<td>{team.name}</td>
								<td class="flex flex-row gap-6 flex-wrap justify-end">
									<a class="btn btn-primary btn-sm" href={routes.team(team.id)}>Zobacz</a>
									<button class="btn btn-error btn-outline btn-sm">Delete</button>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
				<!-- if there is a button in form, it will close the modal -->
				<button class="btn">Close</button>
			</div>
		</form>
	</dialog>
{/if}
