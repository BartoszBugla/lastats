<script>
	import { base } from '$app/paths';
	import ArrowDown from '$lib/icons/arrow-down.svelte';
</script>

<div class="navbar bg-base-100">
	<div class="flex-1">
		<a href="{base}/" class="btn btn-ghost normal-case text-xl">LaStats</a>
	</div>
	<div class="flex-none">
		<ul class="menu menu-horizontal px-1">
			<li><a href="{base}/">Ligi</a></li>
			<li>
				<a href="{base}/" tabindex="0">
					Statystyki
					<ArrowDown />
				</a>
				<ul class="p-2 bg-base-100">
					<li><a href="{base}/">Zawodnicy</a></li>
					<li><a href="{base}/">Druzyny</a></li>
				</ul>
			</li>
			<li>
				<a href="{base}/" tabindex="0">
					Dodaj
					<ArrowDown />
				</a>
				<ul class="p-2 bg-base-100">
					<li><a href="{base}/">Ligę</a></li>
					<li><a href="{base}/">Zawodnika</a></li>
					<li><a href="{base}/">Drużynę</a></li>
				</ul>
			</li>
		</ul>
	</div>
</div>
