import { Api } from './myApi';

const api = new Api({
	baseUrl: 'http://127.0.0.1:8080',
	baseApiParams: {
		headers: {
			'Content-Type': 'application/json'
		}
	}
});

export default api;
