import { onMount } from 'svelte';
import { writable } from 'svelte/store';

interface UseDynamicRouteProps {
	isNumeric?: boolean;
	fallbackAction?: () => void;
}

export const useDynamicRoute = <T = unknown>({
	isNumeric,
	fallbackAction
}: UseDynamicRouteProps = {}) => {
	const parameter = writable<T>();

	onMount(() => {
		const idRaw = document.location.pathname.split('/').pop() || '';

		parameter.set(idRaw as unknown as T);

		if (isNumeric) {
			parameter.set(parseInt(idRaw) as unknown as T);
			if (isNaN(parseInt(idRaw)) && fallbackAction) {
				fallbackAction();
			}
		}
	});

	return parameter;
};
