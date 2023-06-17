import axios from 'axios';
import type { CreateLeagueRequest, League } from './models/leagues';

const apiClient = axios.create({
	baseURL: 'http://localhost:8000',
	withCredentials: false,
	headers: {
		'Access-Control-Allow-Origin': '*',
		'content-type': 'application/json'
	}
});

export const api = {
	test: {
		getAll: () => apiClient.get('/test/').then(({ data }) => data)
	},
	leagues: {
		get: (id: number) => apiClient.get<League>(`/leagues/${id}`).then(({ data }) => data),

		getAll: () => apiClient.get<League[]>('/leagues/').then(({ data }) => data),

		create: (payload: CreateLeagueRequest) =>
			apiClient.post('/leagues/', payload).then(({ data }) => data),

		delete: (id: number) => apiClient.delete(`/leagues/${id}`)
	}
};
