<script lang="ts">
	import { goto } from '$app/navigation';
	import api from '$lib/api';
	import TextField from '$lib/components/TextField.svelte';
	import { routes } from '$lib/config/routes';
	import type { CreateLeagueRequest } from '$lib/myApi';
	import { errorToast, successToast } from '$lib/utils/success-toast';

	import { createMutation, useQueryClient } from '@tanstack/svelte-query';

	import * as z from 'zod';

	let name: string;
	let error = '';

	const client = useQueryClient();

	let schema = z.object({
		name: z.string().min(1, 'Name is Required')
	});

	const addLeague = createMutation({
		mutationFn: (payload: CreateLeagueRequest) =>
			api.leagues.postLeagues(payload).then((res) => res.data),

		onSuccess: (data) => {
			client.invalidateQueries(['leagues']);
			successToast('Dodano ligę');
			goto(routes.league(data.id));
		},
		onError: (err) => {
			errorToast('Nie mozna dodać ligi');
		}
	});

	const validateSchema = (schema: z.AnyZodObject, values: unknown) => {
		try {
			schema.parse(values);
		} catch (err) {
			if (err instanceof z.ZodError) {
				return err.errors[0].message;
			}
		}
	};

	const handleSubmit = (e: Event) => {
		e.preventDefault();

		const formValues: CreateLeagueRequest = {
			name
		};

		const isError = validateSchema(schema, formValues);

		if (isError) {
			error = isError;
			return;
		}
		error = '';
		$addLeague.mutate(formValues);
	};
</script>

<form
	on:submit={handleSubmit}
	class="form-control w-full max-w-xs flex flex-col gap-4 mx-auto mt-10"
>
	<TextField label="Dodaj ligę" bind:value={name} />
	{#if !!error}
		<p class="text-red-500">{error}</p>
	{/if}
	<button class="btn btn-primary" type="submit">Dodaj</button>
</form>
