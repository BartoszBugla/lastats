<script lang="ts">
	import api from '$lib/api';
	import { useDialog } from '$lib/utils/use-dialog';
	import { createQuery } from '@tanstack/svelte-query';
	import AddTeamDialog from './AddTeamForm.svelte';
	import AddTeamForm from './AddTeamForm.svelte';

	export let leagueId: number = 0;
	export let isOpened: boolean = false;
	export let selected: number[] = [];
	export let closeDialog: () => void;
	export let onSubmit: () => void;
	export let onCancel: () => void;

	$: query = createQuery({
		queryKey: ['teams'],
		queryFn: () =>
			api.teams.getTeams().then((res) => res.data.filter((team) => team.league_id !== leagueId)),
		enabled: isOpened
	});

	const select = (id: number) => {
		if (selected.includes(id)) {
			selected = selected.filter((item) => item !== id);
		} else {
			selected = [...selected, id];
		}
	};

	let isAddForm = false;
	const switchView = () => {
		isAddForm = !isAddForm;
	};
</script>

<dialog class="modal" open={isOpened} on:close={closeDialog}>
	<form method="dialog" class="modal-box">
		{#if isAddForm}
			<h3 class="font-bold text-lg h-1/2">Hello!</h3>
			<AddTeamForm {switchView} />
		{:else}
			<h3 class="font-bold text-lg h-1/2">Hello!</h3>
			<p class="py-4">Dodaj zespoły do danej ligi</p>
			<button class="link link-primary" on:click={switchView}>Dodaj nowy</button>

			<div class="modal-action flex flex-col">
				<div class="overflow-auto block max-h-[400px]">
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
								{#each $query.data as team}
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
				</div>
				<!-- if there is a button in form, it will close the modal -->
				<div class="ml-auto flex justify-end gap-2 mt-3">
					<button class="btn btn-secondary btn-sm" on:click={onSubmit}
						>Dodaj ({selected.length})</button
					>
					<button class="btn btn-error btn-outline btn-sm" on:click={onCancel}>Anuluj</button>
				</div>
			</div>
		{/if}
	</form>
</dialog>
