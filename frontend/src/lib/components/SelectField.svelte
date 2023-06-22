<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';

	interface Option {
		value: string | number;
		text: string;
	}
	interface $$restProps extends HTMLAttributes<HTMLSelectElement> {}

	export let options: Option[];
	export let label: string;

	$: console.log(options);
</script>

<div class="flex flex-col">
	<label for={$$restProps.name}>{label}</label>
	<select name={$$restProps.name} {...$$restProps} class="select select-accent mt-2">
		{#each options as option}
			<option value={option.value}>
				{option.text}
			</option>
		{/each}
	</select>
</div>
