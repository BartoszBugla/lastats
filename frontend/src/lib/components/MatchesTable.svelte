<script lang="ts">
	import { routes } from '$lib/config/routes';
	import type { MatchModel } from '$lib/myApi';
	import { format, isAfter } from 'date-fns';

	export let data: MatchModel[] = [];

	let matchEnded = (match: MatchModel) => {
		return isAfter(new Date(), new Date(match.time));
	};
</script>

{#if data}
	{#each data as match}
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
				<tr>
					<td>
						<a class="link link-hover" href={routes.team(match.home_team_id)}>
							{match.home_team?.name || 'Unknown'}
						</a>
					</td>
					{#if matchEnded(match)}
						<td>{match.home_team_goals}-{match.guest_team_goals}</td>
					{:else}
						<td>-</td>
					{/if}
					<td>
						<a class="link link-hover" href={routes.team(match.home_team_id)}>
							{match.guest_team?.name || 'Unknown'}
						</a>
					</td>
					<td>
						{#if matchEnded(match)}
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
			</tbody>
		</table>
	{/each}
{/if}
