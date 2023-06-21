<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';

	export let label: string = '';
	export let value: string = '';

	interface $$Props extends HTMLAttributes<HTMLInputElement> {
		label?: string;
		value: string;
	}
</script>

<div class="form-control w-full max-w-xs">
	{#if label}<label class="label" for="dsds">{label}</label>{/if}
	<input {...$$restProps} type="number" class="input input-bordered w-full max-w-xs" bind:value />
</div>
