<script lang="ts">
	import { api } from '$lib/api';
	import { createQuery } from '@tanstack/svelte-query';
	import { onMount } from 'svelte';

	export const leagueId: number = 0;

	export let isOpened: boolean = false;
	export let selected: number[] = [];
	export let closeDialog: () => void;
	export let onSubmit: () => void;
	export let onCancel: () => void;

	$: query = createQuery({
		queryKey: ['teams'],
		queryFn: () => api.teams.getAll(),
		enabled: isOpened,
		onSuccess(data) {
			console.log(data);
		}
	});

	const select = (id: number) => {
		if (selected.includes(id)) {
			selected = selected.filter((item) => item !== id);
		} else {
			selected = [...selected, id];
		}
	};
</script>

<dialog class="modal" open={isOpened} on:close={closeDialog}>
	<form method="dialog" class="modal-box">
		<h3 class="font-bold text-lg h-1/2">Hello!</h3>
		<p class="py-4">Dodaj zespoły do danej ligi</p>
		<div class="modal-action flex flex-col">
			<table class="table w-full p-2 mb-6">
				<!-- head -->
				<thead>
					<tr>
						<th />
						<th>id</th>
						<th>Name</th>
					</tr>
				</thead>
				<tbody>
					{#if $query.data}
						{#each $query.data.teams.filter((team) => team.leagueId != leagueId) as team}
							<tr>
								<th>
									<label>
										<input
											on:click={() => select(team.id)}
											checked={selected.includes(team.id)}
											type="checkbox"
											class="checkbox"
										/>
									</label>
								</th>
								<td>{team.id}</td>
								<td>{team.name}</td>
							</tr>
						{/each}
					{/if}
				</tbody>
			</table>
			<!-- if there is a button in form, it will close the modal -->
			<div class="ml-auto flex justify-end gap-2">
				<button class="btn btn-secondary btn-sm" on:click={onSubmit}
					>Dodaj ({selected.length})</button
				>
				<button class="btn btn-error btn-outline btn-sm" on:click={onCancel}>Anuluj</button>
			</div>
		</div>
	</form>
</dialog>
