import { writable } from 'svelte/store';

interface Toast {
	id: number;
	message: string;
	type: 'success' | 'error';
}

function createCount() {
	const { subscribe, set, update } = writable<Toast[]>([]);

	return {
		subscribe,
		push: (toast: Toast) => {
			update((state) => [toast, ...state]);
			setTimeout(() => {
				update((state) => state.filter((t) => t.id !== toast.id));
			}, 5000);
		}
	};
}

export const count = createCount();
