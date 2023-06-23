<script lang="ts">
	import api from '$lib/api';
	import { routes } from '$lib/config/routes';
	import { createMutation, createQuery } from '@tanstack/svelte-query';
	import { format, isToday, isBefore, isAfter } from 'date-fns';

	$: query = createQuery({
		queryKey: ['latest-matches'],
		queryFn: () => api.matches.getMatches().then((res) => res.data)
	});
</script>

<h1 class="text-center text-2xl mt-10 font-bold">Witaj w LaStats</h1>
<h2 class="text-center text-lg mt-2">Najlepsza strona z drużynami oraz meczami</h2>

{#if $query.isLoading}
	<span class="loading loading-spinner loading-lg mx-auto" />
{:else if $query.data}
	<table class="table w-full p-2 mb-6 max-w-[900px] mx-auto mt-10 text-center">
		<!-- head -->
		<thead>
			<tr>
				<th>Home</th>
				<th>Result</th>
				<th>Away</th>
				<th />
				<th>Time</th>
				<th>Liga</th>
			</tr>
		</thead>
		<tbody>
			{#each $query.data as match}
				<tr>
					<td>
						<a class="link link-primary" href={routes.team(match.home_team_id)}>
							{match.home_team?.name}
						</a>
					</td>

					<td>{match.home_team_goals}-{match.guest_team_goals}</td>

					<td>
						<a class="link link-primary" href={routes.team(match.home_team_id)}>
							{match.guest_team?.name}
						</a>
					</td>
					<td>
						{#if isAfter(new Date(), new Date(match.time))}
							<div class="badge badge-ghost badge-outline badge-sm">Ended</div>
						{/if}
					</td>
					<td>{format(new Date(match.time), 'dd-MM-yyyy HH:mm')}</td>
					<td>
						<a class="link link-secondary" href={routes.league(match.league_id)}>
							{match.league?.name}
						</a>
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
{/if}
