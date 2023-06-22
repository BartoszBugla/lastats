<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';

	interface $$restProps extends HTMLAttributes<HTMLInputElement> {}

	export let label: string = '';
	export let value: string = '';
</script>

<div class="form-control w-full max-w-xs">
	{#if label}<label class="label" for="dsds">{label}</label>{/if}
	<input
		{...$$restProps}
		type="text"
		class="input input-accent input-bordered w-full max-w-xs"
		bind:value
	/>
</div>
