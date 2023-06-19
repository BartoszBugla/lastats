/* eslint-disable */
/* tslint:disable */
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

export interface Team {
	/** Team ID */
	id: number;
	/** Team name */
	name: string;
	/** League ID */
	league_id: number;
	/** League name */
	league_name: string;
}

export interface CreateTeamRequest {
	/** Team name */
	name: string;
}

export interface CreateLeagueRequest {
	/** League name */
	name: string;
}

export interface League {
	/** League ID */
	id: number;
	/** League name */
	name: string;
	/** List of teams in the league */
	teams: Team[];
}

export interface CreateLeagueResponse {
	/** Created League ID */
	id: number;
}

export interface AddLeagueTeamsRequest {
	/** List of team IDs */
	ids: number[];
}

export type QueryParamsType = Record<string | number, any>;
export type ResponseFormat = keyof Omit<Body, 'body' | 'bodyUsed'>;

export interface FullRequestParams extends Omit<RequestInit, 'body'> {
	/** set parameter to `true` for call `securityWorker` for this request */
	secure?: boolean;
	/** request path */
	path: string;
	/** content type of request body */
	type?: ContentType;
	/** query params */
	query?: QueryParamsType;
	/** format of response (i.e. response.json() -> format: "json") */
	format?: ResponseFormat;
	/** request body */
	body?: unknown;
	/** base url */
	baseUrl?: string;
	/** request cancellation token */
	cancelToken?: CancelToken;
}

export type RequestParams = Omit<FullRequestParams, 'body' | 'method' | 'query' | 'path'>;

export interface ApiConfig<SecurityDataType = unknown> {
	baseUrl?: string;
	baseApiParams?: Omit<RequestParams, 'baseUrl' | 'cancelToken' | 'signal'>;
	securityWorker?: (
		securityData: SecurityDataType | null
	) => Promise<RequestParams | void> | RequestParams | void;
	customFetch?: typeof fetch;
}

export interface HttpResponse<D extends unknown, E extends unknown = unknown> extends Response {
	data: D;
	error: E;
}

type CancelToken = Symbol | string | number;

export enum ContentType {
	Json = 'application/json',
	FormData = 'multipart/form-data',
	UrlEncoded = 'application/x-www-form-urlencoded',
	Text = 'text/plain'
}

export class HttpClient<SecurityDataType = unknown> {
	public baseUrl: string = '/';
	private securityData: SecurityDataType | null = null;
	private securityWorker?: ApiConfig<SecurityDataType>['securityWorker'];
	private abortControllers = new Map<CancelToken, AbortController>();
	private customFetch = (...fetchParams: Parameters<typeof fetch>) => fetch(...fetchParams);

	private baseApiParams: RequestParams = {
		credentials: 'same-origin',
		headers: {},
		redirect: 'follow',
		referrerPolicy: 'no-referrer'
	};

	constructor(apiConfig: ApiConfig<SecurityDataType> = {}) {
		Object.assign(this, apiConfig);
	}

	public setSecurityData = (data: SecurityDataType | null) => {
		this.securityData = data;
	};

	protected encodeQueryParam(key: string, value: any) {
		const encodedKey = encodeURIComponent(key);
		return `${encodedKey}=${encodeURIComponent(typeof value === 'number' ? value : `${value}`)}`;
	}

	protected addQueryParam(query: QueryParamsType, key: string) {
		return this.encodeQueryParam(key, query[key]);
	}

	protected addArrayQueryParam(query: QueryParamsType, key: string) {
		const value = query[key];
		return value.map((v: any) => this.encodeQueryParam(key, v)).join('&');
	}

	protected toQueryString(rawQuery?: QueryParamsType): string {
		const query = rawQuery || {};
		const keys = Object.keys(query).filter((key) => 'undefined' !== typeof query[key]);
		return keys
			.map((key) =>
				Array.isArray(query[key])
					? this.addArrayQueryParam(query, key)
					: this.addQueryParam(query, key)
			)
			.join('&');
	}

	protected addQueryParams(rawQuery?: QueryParamsType): string {
		const queryString = this.toQueryString(rawQuery);
		return queryString ? `?${queryString}` : '';
	}

	private contentFormatters: Record<ContentType, (input: any) => any> = {
		[ContentType.Json]: (input: any) =>
			input !== null && (typeof input === 'object' || typeof input === 'string')
				? JSON.stringify(input)
				: input,
		[ContentType.Text]: (input: any) =>
			input !== null && typeof input !== 'string' ? JSON.stringify(input) : input,
		[ContentType.FormData]: (input: any) =>
			Object.keys(input || {}).reduce((formData, key) => {
				const property = input[key];
				formData.append(
					key,
					property instanceof Blob
						? property
						: typeof property === 'object' && property !== null
						? JSON.stringify(property)
						: `${property}`
				);
				return formData;
			}, new FormData()),
		[ContentType.UrlEncoded]: (input: any) => this.toQueryString(input)
	};

	protected mergeRequestParams(params1: RequestParams, params2?: RequestParams): RequestParams {
		return {
			...this.baseApiParams,
			...params1,
			...(params2 || {}),
			headers: {
				...(this.baseApiParams.headers || {}),
				...(params1.headers || {}),
				...((params2 && params2.headers) || {})
			}
		};
	}

	protected createAbortSignal = (cancelToken: CancelToken): AbortSignal | undefined => {
		if (this.abortControllers.has(cancelToken)) {
			const abortController = this.abortControllers.get(cancelToken);
			if (abortController) {
				return abortController.signal;
			}
			return void 0;
		}

		const abortController = new AbortController();
		this.abortControllers.set(cancelToken, abortController);
		return abortController.signal;
	};

	public abortRequest = (cancelToken: CancelToken) => {
		const abortController = this.abortControllers.get(cancelToken);

		if (abortController) {
			abortController.abort();
			this.abortControllers.delete(cancelToken);
		}
	};

	public request = async <T = any, E = any>({
		body,
		secure,
		path,
		type,
		query,
		format,
		baseUrl,
		cancelToken,
		...params
	}: FullRequestParams): Promise<HttpResponse<T, E>> => {
		const secureParams =
			((typeof secure === 'boolean' ? secure : this.baseApiParams.secure) &&
				this.securityWorker &&
				(await this.securityWorker(this.securityData))) ||
			{};
		const requestParams = this.mergeRequestParams(params, secureParams);
		const queryString = query && this.toQueryString(query);
		const payloadFormatter = this.contentFormatters[type || ContentType.Json];
		const responseFormat = format || requestParams.format;

		return this.customFetch(
			`${baseUrl || this.baseUrl || ''}${path}${queryString ? `?${queryString}` : ''}`,
			{
				...requestParams,
				headers: {
					...(requestParams.headers || {}),
					...(type && type !== ContentType.FormData ? { 'Content-Type': type } : {})
				},
				signal: cancelToken ? this.createAbortSignal(cancelToken) : requestParams.signal,
				body: typeof body === 'undefined' || body === null ? null : payloadFormatter(body)
			}
		).then(async (response) => {
			const r = response as HttpResponse<T, E>;
			r.data = null as unknown as T;
			r.error = null as unknown as E;

			const data = !responseFormat
				? r
				: await response[responseFormat]()
						.then((data) => {
							if (r.ok) {
								r.data = data;
							} else {
								r.error = data;
							}
							return r;
						})
						.catch((e) => {
							r.error = e;
							return r;
						});

			if (cancelToken) {
				this.abortControllers.delete(cancelToken);
			}

			if (!response.ok) throw data;
			return data;
		});
	};
}

/**
 * @title Lastats API
 * @version 1.0
 * @baseUrl /
 *
 * API documentation for the backend of Lastats
 */
export class Api<SecurityDataType extends unknown> extends HttpClient<SecurityDataType> {
	leagues = {
		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name GetLeagues
		 * @summary Returns list of all the leagues
		 * @request GET:/leagues
		 */
		getLeagues: (params: RequestParams = {}) =>
			this.request<League[], any>({
				path: `/leagues`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name PostLeagues
		 * @summary Creates a new league
		 * @request POST:/leagues
		 */
		postLeagues: (payload: CreateLeagueRequest, params: RequestParams = {}) =>
			this.request<CreateLeagueResponse, void>({
				path: `/leagues`,
				method: 'POST',
				body: payload,
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name PutLeagueById
		 * @summary Updates league's data
		 * @request PUT:/leagues/{league_id}
		 */
		putLeagueById: (leagueId: number, payload: CreateLeagueRequest, params: RequestParams = {}) =>
			this.request<CreateLeagueResponse, void>({
				path: `/leagues/${leagueId}`,
				method: 'PUT',
				body: payload,
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name DeleteLeagueById
		 * @summary Deletes the league with the specified ID
		 * @request DELETE:/leagues/{league_id}
		 */
		deleteLeagueById: (leagueId: number, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/leagues/${leagueId}`,
				method: 'DELETE',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name GetLeagueById
		 * @summary Returns the league with the specified ID
		 * @request GET:/leagues/{league_id}
		 */
		getLeagueById: (leagueId: number, params: RequestParams = {}) =>
			this.request<League, void>({
				path: `/leagues/${leagueId}`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name PostLeagueTeams
		 * @summary Deletes the league with the specified ID
		 * @request POST:/leagues/{league_id}/teams
		 */
		postLeagueTeams: (
			leagueId: number,
			payload: AddLeagueTeamsRequest,
			params: RequestParams = {}
		) =>
			this.request<void, void>({
				path: `/leagues/${leagueId}/teams`,
				method: 'POST',
				body: payload,
				type: ContentType.Json,
				...params
			})
	};
	teams = {
		/**
		 * No description
		 *
		 * @tags Teams
		 * @name GetListAllTeams
		 * @summary Returns list of all the teams whose names contain the given query
		 * @request GET:/teams
		 */
		getListAllTeams: (params: RequestParams = {}) =>
			this.request<Team[], any>({
				path: `/teams`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name PutTeam
		 * @summary Updates team's data
		 * @request PUT:/teams/{team_id}
		 */
		putTeam: (teamId: number, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/teams/${teamId}`,
				method: 'PUT',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name DeleteTeam
		 * @summary Deletes the team with the specified ID
		 * @request DELETE:/teams/{team_id}
		 */
		deleteTeam: (teamId: number, params: RequestParams = {}) =>
			this.request<void, any>({
				path: `/teams/${teamId}`,
				method: 'DELETE',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name GetTeam
		 * @summary Returns the team with the specified ID
		 * @request GET:/teams/{team_id}
		 */
		getTeam: (teamId: number, params: RequestParams = {}) =>
			this.request<Team, void>({
				path: `/teams/${teamId}`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name PostTeam
		 * @summary Creates a new team
		 * @request POST:/teams/{team_id}
		 */
		postTeam: (teamId: number, payload: CreateTeamRequest, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/teams/${teamId}`,
				method: 'POST',
				body: payload,
				type: ContentType.Json,
				...params
			})
	};
}
