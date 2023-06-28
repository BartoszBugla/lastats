<script lang="ts">
	import TextField from '$lib/components/TextField.svelte';
	import { routes } from '$lib/config/routes';
	import { quantiles, quantilesBase } from '$lib/helpers';
	import { error } from '@sveltejs/kit';

	interface ConfRange {
		x?: number[];
		sigma2?: number;
		alpha?: number;
		meanX?: number;
		confFactor?: number;
		n?: number;
		h0: number;
	}

	let x: string = '6.8, 6.9, 7.2, 7.0, 7.8, 7.7, 7.3, 7.2';
	let sigma2: number;
	let alpha: number = 0.1;
	let meanX: number;
	let confFactor: number;
	let n: number;
	let h0: number = 7.1;

	const Sn = (x: number[]) => {
		const mean = x.reduce((a, b) => a + b, 0) / x.length || 0;

		x = x.map((x) => Math.pow(x, 2));

		const sum = x.reduce((a, b) => a + b, 0);

		return sum / x.length - Math.pow(mean, 2);
	};

	const round = (num: number, dec: number) =>
		Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);

	const confRange = ({ x, sigma2, alpha, meanX, confFactor, n, h0 }: ConfRange) => {
		if (confFactor) alpha = round(1 - confFactor, 2);

		if (!n) {
			if (!x) throw new Error('Brakujące dane x');
			n = x.length;
		}

		if (!meanX) {
			if (!x) throw new Error('Brakujące dane x');
			const sum = x.reduce((a, b) => a + b, 0);
			meanX = sum / x.length || 0;
		}

		if (!sigma2) {
			if (!alpha || !x) throw new Error('Brakujące dane alpha lub x');

			let sigma = round(Math.sqrt(Sn(x)), 2);

			let quantile = quantiles[(1 - alpha / 2) as unknown as keyof typeof quantilesBase][n - 2];

			let testStat = round((Math.sqrt(n - 1) * (meanX - h0)) / sigma, 2);

			let division = `[${-quantile}, ${quantile}]`;

			return {
				alpha,
				n,
				meanX,
				sigma,
				quantile,
				testStat,
				division
			};
		} else {
			if (!alpha) throw new Error('Brakujące dane alpha');

			let sigma = round(Math.sqrt(sigma2), 2);

			let quantile = quantilesBase[(1 - alpha / 2) as unknown as keyof typeof quantilesBase];

			let main = round((quantile * sigma) / Math.sqrt(n), 2);

			let testStat = round((Math.sqrt(n) * (meanX - h0)) / sigma, 2);

			let division = `[${-quantile}, ${quantile}]`;

			return {
				testStat,
				alpha,
				n,
				meanX,
				sigma,
				quantile,
				main,
				division
			};
		}
	};

	const getResult = (payload: ConfRange) => {
		try {
			const parsedX = x.split(',').map((x) => parseFloat(x) || 0) || null;

			return confRange({ ...payload, x: parsedX });
		} catch (error: any) {
			console.log(error.message);
			return null;
		}
	};

	$: result = getResult({ n, confFactor, meanX, sigma2, alpha, x: x as any, h0 });
</script>

<div class="max-w-lg px-5 mx-auto">
	{#if result}
		<p>
			Sigma: {result.sigma},
		</p>
		<p>
			k(1-alfa/2): {result.quantile}
		</p>
		<p>
			alfa: {result.alpha}
		</p>
		<p>
			n: {result.n}
		</p>
		<p>
			Przedział: {result.division}
		</p>

		<p>
			Testowa Statystyka: {result.testStat}
		</p>
	{/if}

	<hr class="my-4" />
	<div>
		<div class="flex flex-col">
			<label>X: </label>
			<input class="input input-accent" bind:value={x} />
		</div>

		<div class="flex flex-col">
			<label>meanX: </label>
			<input class="input input-accent" type="number" bind:value={meanX} />
		</div>

		<div class="flex flex-col">
			<label>sigma2: </label>
			<input class="input input-accent" type="number" bind:value={sigma2} />
		</div>
		<div class="flex flex-col">
			<label>alpha: </label>
			<input class="input input-accent" type="number" bind:value={alpha} />
		</div>

		<div class="flex flex-col">
			<label>factor: </label>
			<input class="input input-accent" type="number" bind:value={confFactor} />
		</div>

		<div class="flex flex-col">
			<label>n: </label>
			<input class="input input-accent" type="number" bind:value={n} />
		</div>

		<div class="flex flex-col">
			<label>h0: </label>
			<input class="input input-accent" type="number" bind:value={h0} />
		</div>
	</div>
	<a class="link" href={routes.home()}>Liczenie przedziałów </a>
</div>
