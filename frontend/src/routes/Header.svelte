<script lang="ts">
	import { base } from '$app/paths';
	import AddTeamForm from '$lib/components/AddTeamForm.svelte';
	import { routes } from '$lib/config/routes';
	import { useDialog } from '$lib/utils/use-dialog';

	const [isOpenDialog, openDialog, closeDialog] = useDialog();
</script>

<div class="navbar bg-base-100 sticky top-0 z-10 shadow-lg px-12">
	<div class="flex-1">
		<a href="{base}/" class="btn btn-ghost normal-case text-xl">LaStats</a>
	</div>
	<div class="flex-none">
		<ul class="menu menu-horizontal px-1">
			<li><a href={routes.leagues()}>Ligi</a></li>
			<li><a href={routes.teams()}>Zespoły</a></li>

			<li class="bg-base-100">
				<details>
					<summary>Dodaj</summary>
					<ul>
						<li><a href={routes.addLeague()}>Ligę</a></li>
						<li><button on:click={openDialog} class="link">Drużynę</button></li>
					</ul>
				</details>
			</li>
		</ul>
	</div>

	<dialog class="modal" open={$isOpenDialog} on:close={closeDialog}>
		<form method="dialog" class="modal-box">
			<AddTeamForm switchView={closeDialog} />
		</form>
	</dialog>
</div>
