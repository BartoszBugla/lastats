<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
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
					{#each data.leagues as league}
						<tr>
							<th />
							<td>{league.id}</td>
							<td>{league.name}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>
</section>
