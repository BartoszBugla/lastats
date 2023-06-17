import { base } from '$app/paths';

export const routes = {
	home: () => `${base}/`,
	leagues: () => `${base}/leagues`,
	addLeague: () => `${base}/leagues/add`,
	league: (id: number) => `${base}/leagues/${id}`
};
