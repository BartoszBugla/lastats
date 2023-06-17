<script lang="ts">
	import { api, type League } from '$lib/api';
	import TextField from '$lib/components/TextField.svelte';
	import { routes } from '$lib/config/routes';
	import { createMutation, createQuery, useQueryClient } from '@tanstack/svelte-query';

	let searchValue = '';

	const client = useQueryClient();

	const query = createQuery({
		queryKey: ['leagues'],
		queryFn: () => api.leagues.getAll()
	});

	$: data = $query.data?.filter((league) => league.name.includes(searchValue)) || [];

	const deleteAction = createMutation({
		mutationFn: (id: number) => api.leagues.delete(id),
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

		<div class="overflow-x-auto mx-auto w-auto px-6">
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
					{#if $query.isLoading}
						<span class="loading loading-spinner loading-lg mx-auto" />
					{:else if $query.isSuccess}
						{#each data as league}
							<tr>
								<td />
								<td>{league.id}</td>
								<td>{league.name}</td>

								<td class="flex flex-row gap-6 flex-wrap justify-end">
									<a class="btn btn-primary btn-sm" href={routes.league(league.id)}>Zobacz</a>
									<button
										class="btn btn-error btn-outline btn-sm"
										on:click={() => $deleteAction.mutateAsync(league.id)}>Delete</button
									>
								</td>
							</tr>
						{/each}
					{/if}
				</tbody>
			</table>
		</div>
	</div>
</section>
