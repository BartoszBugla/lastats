import axios from 'axios';

const apiClient = axios.create({
	baseURL: 'http://localhost:8000/',
	withCredentials: false
});

export const api = {
	test: {
		getAll: () => apiClient.get('/test/').then(({ data }) => data)
	},
	league: {
		getAll: () => apiClient.get('/league/').then(({ data }) => data),
		create: (name: string) => apiClient.post('/league/', { name }).then(({ data }) => data)
	}
};
