import axios from 'axios';
import type { CreateLeagueRequest, League } from './models/leagues';

const apiClient = axios.create({
	baseURL: 'http://localhost:8000',
	withCredentials: false
});

export const api = {
	test: {
		getAll: () => apiClient.get('/test/').then(({ data }) => data)
	},
	leagues: {
		getById: (id: number) => apiClient.get<League>(`/leagues/${id}`),
		getAll: () => apiClient.get<League[]>('/leagues/').then(({ data }) => data),
		create: (payload: CreateLeagueRequest) =>
			apiClient.post('/leagues/', payload).then(({ data }) => data)
	}
};
