<script lang="ts">
	import api from '$lib/api';
	import { createMutation, createQuery, useQueryClient } from '@tanstack/svelte-query';
	import TextField from './TextField.svelte';

	import * as z from 'zod';
	import type { CreateTeamRequest } from '$lib/myApi';

	import { errorToast, successToast } from '$lib/utils/success-toast';

	import NumberField from './NumberField.svelte';

	export let switchView: () => void;
	const client = useQueryClient();

	let name: string;
	let wins: string = '0';
	let draws: string = '0';
	let losses: string = '0';

	let error = '';

	let schema = z.object({
		name: z.string().min(1, 'Name is Required'),
		wins: z
			.number({ coerce: true, invalid_type_error: 'Wins must be a number' })
			.min(0, 'Wins must be a positive number'),

		draws: z
			.number({ coerce: true, invalid_type_error: 'Draws must be a number' })
			.min(0, 'Draws must be a positive number'),
		losses: z
			.number({ coerce: true, invalid_type_error: 'Losses must be a number' })
			.min(0, 'Losses must be a positive number')
	});

	const validateSchema = (schema: z.AnyZodObject, values: unknown) => {
		try {
			return [schema.parse(values), undefined];
		} catch (err) {
			if (err instanceof z.ZodError) {
				console.log(err.errors);
				return [undefined, err.errors[0].message];
			}
		}
	};

	const addTeam = createMutation({
		mutationFn: (payload: CreateTeamRequest) =>
			api.teams.postTeams(payload).then((res) => res.data),

		onSuccess: (data) => {
			client.invalidateQueries(['teams']);
			successToast('Dodano Zespół');
			switchView();
		},

		onError: (err) => {
			errorToast('Nie mozna dodać ligi');
		}
	});

	const handleSubmit = (e: Event) => {
		e.preventDefault();

		const formValues = {
			name,
			wins,
			draws,
			losses
		};

		const [parsed, isError] = validateSchema(schema, formValues) as [
			z.infer<typeof schema>,
			string
		];

		if (isError) {
			error = isError;
			return;
		}
		error = '';
		$addTeam.mutate(parsed);
	};
</script>

<form on:submit={handleSubmit}>
	<TextField bind:value={name} label="Nazwa *" placeholder="Legia Warszawa" />
	<p class="text-sm text-center my-2">
		Pola poniej muszą byc liczbowe w przypadku nie podania wartośći automatycznie jest 0
	</p>
	<NumberField bind:value={wins} label="Wins" />
	<NumberField bind:value={draws} label="Draws" />
	<NumberField bind:value={losses} label="Losses" />
	{#if error}
		<p class="text-red-500">{error}</p>
	{/if}

	<button type="submit" class="mt-2 btn btn-primary float-right ml-5"> Dodaj </button>
	<button type="button" class="mt-2 btn float-right" on:click={switchView}> Anuluj </button>
</form>
