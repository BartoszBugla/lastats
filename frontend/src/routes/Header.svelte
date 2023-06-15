<script lang="ts">
	import { base } from '$app/paths';
	import { routes } from '$lib/config/routes';
</script>

<div class="navbar bg-base-100 sticky top-0 z-10 shadow-lg px-12">
	<div class="flex-1">
		<a href="{base}/" class="btn btn-ghost normal-case text-xl">LaStats</a>
	</div>
	<div class="flex-none">
		<ul class="menu menu-horizontal px-1">
			<li><a href={routes.leagues()}>Ligi</a></li>
			<li class="bg-base-100">
				<details>
					<summary>Statystyki</summary>
					<ul>
						<li><a href="{base}/">Zawodnicy</a></li>
						<li><a href="{base}/">Druzyny</a></li>
					</ul>
				</details>
			</li>
			<li class="bg-base-100">
				<details>
					<summary>Dodaj</summary>
					<ul>
						<li><a href={routes.addLeague()}>Ligę</a></li>
						<li><a href="{base}/">Zawodnika</a></li>
						<li><a href="{base}/">Drużynę</a></li>
					</ul>
				</details>
			</li>
		</ul>
	</div>
</div>
