<script lang="ts">
	import TextField from '$lib/components/TextField.svelte';
	import { error } from '@sveltejs/kit';

	interface ConfRange {
		x?: number[];
		sigma2?: number;
		alpha?: number;
		meanX?: number;
		confFactor?: number;
		n?: number;
	}

	let x: string = '';
	let sigma2: number = 16;
	let alpha: number = 0.01;
	let meanX: number = 10.2;
	let confFactor: number = 0.99;
	let n: number = 16;

	const quantilesBase = {
		0.9: 1.28,
		0.95: 1.64,
		0.99: 2.33,
		0.995: 2.58
	};

	const quantiles = {
		0.9: [
			3.078, 1.886, 1.638, 1.533, 1.476, 1.44, 1.415, 1.397, 1.383, 1.372, 1.363, 1.356, 1.35,
			1.345, 1.341
		],
		0.95: [
			6.314, 2.92, 2.353, 2.132, 2.015, 1.943, 1.895, 1.859, 1.833, 1.812, 1.795, 1.782, 1.771,
			1.761, 1.753
		],
		0.975: [
			12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.16,
			2.145, 2.131
		],
		0.99: [
			31.821, 6.965, 4.541, 3.747, 3.365, 3.143, 2.998, 3.897, 3.821, 3.764, 2.718, 2.681, 2.65,
			2.624, 2.602
		],
		0.995: [
			63.657, 9.925, 5.841, 4.604, 4.032, 3.707, 3.499, 3.355, 3.25, 3.169, 3.106, 3.054, 3.012,
			2.977, 2.947
		]
	};

	const Sn = (x: number[]) => {
		const sum = x.reduce((a, b) => a + b, 0);
		const mean = sum / x.length || 0;

		return sum / x.length - Math.pow(mean, 2);
	};

	const round = (num: number, dec: number) =>
		Math.round(num * Math.pow(10, dec)) / Math.pow(10, dec);

	const confRange = ({ x, sigma2, alpha, meanX, confFactor, n }: ConfRange) => {
		if (confFactor) alpha = round(1 - confFactor, 2);

		if (!n) {
			if (!x) throw new Error('Brakujące dane');
			n = x.length;
		}

		if (!meanX) {
			if (!x) throw new Error('Brakujące dane');
			const sum = x.reduce((a, b) => a + b, 0);
			meanX = sum / x.length || 0;
		}

		if (!sigma2) {
			if (!alpha || !x) throw new Error('Brakujące dane');

			let sigma = round(Math.sqrt(Sn(x)), 2);
			let quantile = quantiles[(1 - alpha / 2) as unknown as keyof typeof quantilesBase][n];

			let main = round((quantile * sigma) / Math.sqrt(n - 1), 2);

			let division = `${round(meanX - main, 2)} < m < ${round(meanX + main, 2)}`;
			return {
				alpha,
				n,
				meanX,
				sigma,
				quantile,
				main,
				division
			};
		} else {
			if (!alpha) throw new Error('Brakujące dane');

			let sigma = round(Math.sqrt(sigma2), 2);

			let quantile = quantilesBase[(1 - alpha / 2) as unknown as keyof typeof quantilesBase];

			let main = round((quantile * sigma) / Math.sqrt(n), 2);
			console.log(round(meanX + main, 2));
			let division = `${round(meanX - main, 2)} < m < ${round(meanX + main, 2)}`;

			return {
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
	$: result = getResult({ n: parseFloat(n), confFactor, meanX, sigma2, alpha, x: x as any });

	$: console.log(result);
</script>

<div class="ml-5">
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
	{/if}

	<div>
		<div>
			<label>X: </label>
			<input bind:value={x} />
		</div>

		<div>
			<label>meanX: </label>
			<input type="number" bind:value={meanX} />
		</div>

		<div>
			<label>sigma2: </label>
			<input type="number" bind:value={sigma2} />
		</div>
		<div>
			<label>alpha: </label>
			<input type="number" bind:value={alpha} />
		</div>

		<div>
			<label>factor: </label>
			<input type="number" bind:value={confFactor} />
		</div>

		<div>
			<label>n: </label>
			<input type="number" bind:value={n} />
		</div>
	</div>
</div>
