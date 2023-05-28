<script>
	import ArrowDown from '$lib/icons/arrow-down.svelte';
</script>

<div class="navbar bg-base-100">
	<div class="flex-1">
		<a href="/" class="btn btn-ghost normal-case text-xl">LaStats</a>
	</div>
	<div class="flex-none">
		<ul class="menu menu-horizontal px-1">
			<li><a href="#">Ligi</a></li>
			<li>
				<a href="#" tabindex="0">
					Statystyki
					<ArrowDown />
				</a>
				<ul class="p-2 bg-base-100">
					<li><a href="#">Zawodnicy</a></li>
					<li><a href="#">Druzyny</a></li>
				</ul>
			</li>
			<li>
				<a href="#" tabindex="0">
					Dodaj
					<ArrowDown />
				</a>
				<ul class="p-2 bg-base-100">
					<li><a href="#">Ligę</a></li>
					<li><a href="#">Zawodnika</a></li>
					<li><a href="#">Drużynę</a></li>
				</ul>
			</li>
		</ul>
	</div>
</div>
