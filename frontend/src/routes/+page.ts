import { api, type Test } from '$lib/api';
import type { PageLoad } from './$types';

interface MainPageData {
	tests: Test[];
}

export const load: PageLoad<MainPageData> = async () => {
	const tests = await api.test.getAll();
	return { tests };
};
