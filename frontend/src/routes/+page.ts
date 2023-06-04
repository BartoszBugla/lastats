import { api, type League } from '$lib/api';
import type { PageLoad } from './$types';

interface MainPageData {
	leagues: League[];
}

export const load: PageLoad<MainPageData> = async () => {
	const leagues = await api.leagues.getAll();

	console.log(leagues);

	return { leagues };
};
