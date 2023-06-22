<script lang="ts">
	import type { LeagueModel } from '$lib/myApi';
	import * as z from 'zod';
	import TextField from './TextField.svelte';
	import SelectField from './SelectField.svelte';
	import NumberField from './NumberField.svelte';
	import { format, isAfter } from 'date-fns';
	import type { FormEventHandler } from 'svelte/elements';

	enum FormFields {
		HomeTeamId = 'home_team_id',
		GuestTeamId = 'guest_team_id',
		HomeTeamGoals = 'home_team_goals',
		GuestTeamGoals = 'guest_team_goals',
		Location = 'location',
		Time = 'time'
	}

	export let isOpened: boolean;
	export let data: LeagueModel | undefined;
	export let onSubmit: (values: any) => void;
	export let onCancel: () => void;
	export let closeDialog: () => void;

	let error = '';
	let dateValue: Date;
	let showGoals = false;

	$: console.log(dateValue);
	let schema = z.object({
		[FormFields.HomeTeamId]: z.number({ coerce: true, invalid_type_error: 'Id musi być liczbą' }),
		[FormFields.GuestTeamId]: z.number({ coerce: true, invalid_type_error: 'Id musi być liczbą' }),
		[FormFields.Location]: z.string().min(1, 'Lokalizacja jest wymagana'),
		[FormFields.Time]: z.date({ coerce: true })
	});

	const handleSubmit = (e: any) => {
		const formData = new FormData(e.target as HTMLFormElement);
		const data = Object.fromEntries(formData.entries());

		try {
			const parsedData = schema.parse(data);

			if (parsedData.guest_team_id === parsedData.home_team_id) {
				error = 'Zespoły muszą być unikalne';
				return;
			}

			error = '';

			closeDialog();

			onSubmit(parsedData);
		} catch (err) {
			if (err instanceof z.ZodError) {
				error = err.errors[0].message;
			}
		}
	};

	$: options = (data?.teams || []).map(({ name, id }) => ({
		value: id,
		text: name
	}));
</script>

<dialog class="modal" open={isOpened}>
	<form on:submit|preventDefault={handleSubmit} class="modal-box flex flex-col gap-4">
		<SelectField name={FormFields.HomeTeamId} label="Gospodarz meczu" {options} />
		<SelectField name={FormFields.GuestTeamId} label="Gość meczu" {options} />

		<TextField name={FormFields.Location} label="Lokalizacja Spotkania" />
		<p>Czas Spotkania</p>
		<input
			bind:value={dateValue}
			class="input input-accent"
			type="datetime-local"
			name={FormFields.Time}
		/>

		{#if isAfter(new Date(), new Date(dateValue))}
			<div class="flex flex-row gap-4">
				<NumberField min="0" name={FormFields.HomeTeamGoals} defaultValue="0" label="Gole Gosp." />
				<NumberField min="0" name={FormFields.GuestTeamGoals} defaultValue="0" label="Gole Gośći" />
			</div>
		{/if}

		<p class="text-red-600">{error}</p>
		<div class="flex flex-row gap-2 ml-auto">
			<button type="button" on:click={closeDialog} class="btn">Anuluj</button>
			<button type="submit" class="btn btn-primary">Zatwierdź</button>
		</div>
	</form>
</dialog>
