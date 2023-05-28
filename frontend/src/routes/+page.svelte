<script lang="ts">
	import { api } from '$lib/api';
	import type { Test } from '$lib/api/models';
	import { createQuery } from '@tanstack/svelte-query';

	$: tests = createQuery<Test[]>({
		queryKey: ['get-all-tests'],
		queryFn: async () => await api.test.getAll()
	});
</script>

<section class="flex flex-col">
	<div>
		<div class="hero">
			<div class="hero-content text-center">
				<div class="max-w-md">
					<h1 class="text-5xl font-bold">Hello there</h1>
					<p class="py-6">
						Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi
						exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.
					</p>
				</div>
			</div>
		</div>

		<div class="overflow-x-auto mx-auto w-1/2">
			<table class="table w-full">
				<!-- head -->
				<thead>
					<tr>
						<th />
						<th>id</th>
						<th>Name</th>
					</tr>
				</thead>
				<tbody>
					{#if $tests.isLoading}
						<tr>
							<td colspan="3">Loading...</td>
							dsdsds
						</tr>
					{/if}

					{#if $tests.isSuccess}
						{#each $tests.data as item}
							<tr>
								<th />
								<td>{item.id}</td>
								<td>{item.name}</td>
							</tr>
						{/each}
					{/if}
				</tbody>
			</table>
		</div>
	</div>
</section>
