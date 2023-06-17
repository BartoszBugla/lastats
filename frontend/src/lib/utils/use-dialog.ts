import { writable, type Writable } from 'svelte/store';

export const useDialog = (): [Writable<boolean>, () => void, () => void] => {
	const isOpen = writable(false);

	const open = () => {
		isOpen.set(true);
	};

	const close = () => {
		isOpen.set(false);
	};

	return [isOpen, open, close];
};
