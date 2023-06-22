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

export interface CreateTeamRequest {
	/** Team name */
	name: string;
	/** Number of goals */
	goals?: number;
	/** Number of draws */
	draws?: number;
	/** Number of losses */
	losses?: number;
	/** Number of points */
	league_points?: number;
	/** League ID */
	league_id?: number;
}

export type TeamModel = BaseModel & {
	/** Team name */
	name: string;
	/** League ID */
	league_id: number;
	/** Number of wins */
	wins: number;
	/** Number of draws */
	draws: number;
	/** Number of losses */
	losses: number;
	/** League points */
	league_points: number;
	/** List of players */
	players: PlayerModel[];
};

export interface BaseModel {
	/** ID */
	id: number;
	/**
	 * Updated at
	 * @format date-time
	 */
	updated_at: string;
	/**
	 * Created at
	 * @format date-time
	 */
	created_at: string;
}

export type PlayerModel = BaseModel & {
	/** Player name */
	name: string;
	/** Player position */
	position: string;
	/** Player team ID */
	team_id: number;
	/** Player number */
	number?: number;
};

export interface CreateLeagueRequest {
	/** League name */
	name: string;
}

export type LeagueModel = BaseModel & {
	/** League name */
	name: string;
	/** List of teams in the league */
	teams: TeamModel[];
};

export interface CreateLeagueResponse {
	/** Created League ID */
	id: number;
}

export interface AddLeagueTeamsRequest {
	/** List of team IDs */
	ids: number[];
}

export interface AddMatchToLeagueRequest {
	/** Home team ID */
	home_team_id: number;
	/** Guest team ID */
	guest_team_id: number;
	/**
	 * Match time
	 * @format date-time
	 */
	time: string;
	/** Match location */
	location: string;
}

export type MatchModel = BaseModel & {
	/** Home team ID */
	home_team_id: number;
	/** Guest team ID */
	guest_team_id: number;
	home_team?: TeamModel;
	guest_team?: TeamModel;
	/** Home team goals */
	home_team_goals: number;
	/** Guest team goals */
	guest_team_goals: number;
	/** League ID */
	league_id: number;
	league?: LeagueModel;
	match_events?: MatchEventModel[];
	/** Match location */
	location: string;
	/**
	 * Match event time
	 * @format date-time
	 */
	time: string;
};

export type MatchEventModel = BaseModel & {
	/** Match ID */
	match_id: number;
	/** Match minute */
	match_minute: number;
	/** Player ID */
	player_id: number;
	/** Match event type */
	type: string;
};

export interface CreateMatchRequest {
	/** Time when the match started */
	time: string;
	/** Place where the match took place */
	location?: string;
	/** Team ID of the home team */
	home_team_id: number;
	/** Team ID of the guest team */
	guest_team_id: number;
	/** League ID */
	league_id?: number;
	/** Number of goals scored by the guest team */
	guest_team_goals?: number;
	/** Number of goals scored by the home team */
	home_team_goals?: number;
}

export interface CreatePlayerRequest {
	/** Player name */
	name: string;
	/**
	 * Player position
	 * @example "GOALKEEPER"
	 */
	position: 'GOALKEEPER' | 'DEFENDER' | 'MIDFIELDER' | 'FORWARD';
	/** Player's team ID */
	team_id: number;
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
			this.request<LeagueModel[], any>({
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
		 * @name GetLeagueById
		 * @summary Returns the league with the specified ID
		 * @request GET:/leagues/{league_id}
		 */
		getLeagueById: (leagueId: number, params: RequestParams = {}) =>
			this.request<LeagueModel, void>({
				path: `/leagues/${leagueId}`,
				method: 'GET',
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
		 * @name GetLeagueMathes
		 * @request GET:/leagues/{league_id}/matches
		 */
		getLeagueMathes: (leagueId: number, params: RequestParams = {}) =>
			this.request<MatchModel[], any>({
				path: `/leagues/${leagueId}/matches`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name PostLeagueMathes
		 * @summary Create match withing the league
		 * @request POST:/leagues/{league_id}/matches
		 */
		postLeagueMathes: (
			leagueId: number,
			payload: AddMatchToLeagueRequest,
			params: RequestParams = {}
		) =>
			this.request<void, void>({
				path: `/leagues/${leagueId}/matches`,
				method: 'POST',
				body: payload,
				type: ContentType.Json,
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Leagues
		 * @name PostLeagueTeams
		 * @summary Appends teams with the specified IDs to the league
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
	matches = {
		/**
		 * No description
		 *
		 * @tags Matches
		 * @name GetMatches
		 * @summary Returns 10 first matches ordered descending by date
		 * @request GET:/matches
		 */
		getMatches: (
			query?: {
				/** League ID */
				latest?: string;
			},
			params: RequestParams = {}
		) =>
			this.request<MatchModel[], any>({
				path: `/matches`,
				method: 'GET',
				query: query,
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Matches
		 * @name PostMatches
		 * @summary Creates a new player
		 * @request POST:/matches
		 */
		postMatches: (payload: CreateMatchRequest, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/matches`,
				method: 'POST',
				body: payload,
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Matches
		 * @name GetMatchById
		 * @summary Returns the match with the specified ID
		 * @request GET:/matches/{match_id}
		 */
		getMatchById: (matchId: number, params: RequestParams = {}) =>
			this.request<MatchModel, void>({
				path: `/matches/${matchId}`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Matches
		 * @name DeleteMatchById
		 * @summary Deletes the match with the specified ID
		 * @request DELETE:/matches/{match_id}
		 */
		deleteMatchById: (matchId: number, params: RequestParams = {}) =>
			this.request<void, any>({
				path: `/matches/${matchId}`,
				method: 'DELETE',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Matches
		 * @name PutMatchById
		 * @summary Updates match data
		 * @request PUT:/matches/{match_id}
		 */
		putMatchById: (matchId: number, payload: CreateMatchRequest, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/matches/${matchId}`,
				method: 'PUT',
				body: payload,
				...params
			})
	};
	players = {
		/**
		 * No description
		 *
		 * @tags Players
		 * @name GetPlayers
		 * @summary Returns list of all the players whose names contain the given query
		 * @request GET:/players
		 */
		getPlayers: (params: RequestParams = {}) =>
			this.request<PlayerModel[], any>({
				path: `/players`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Players
		 * @name PostPlayers
		 * @summary Creates a new player
		 * @request POST:/players
		 */
		postPlayers: (payload: CreatePlayerRequest, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/players`,
				method: 'POST',
				body: payload,
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Players
		 * @name GetTeamById
		 * @summary Returns the player with the specified ID
		 * @request GET:/players/{player_id}
		 */
		getTeamById: (playerId: number, params: RequestParams = {}) =>
			this.request<PlayerModel, void>({
				path: `/players/${playerId}`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Players
		 * @name DeleteTeamById
		 * @summary Deletes the player with the specified ID
		 * @request DELETE:/players/{player_id}
		 */
		deleteTeamById: (playerId: number, params: RequestParams = {}) =>
			this.request<void, any>({
				path: `/players/${playerId}`,
				method: 'DELETE',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Players
		 * @name PutTeamById
		 * @summary Updates player's data
		 * @request PUT:/players/{player_id}
		 */
		putTeamById: (playerId: number, payload: CreatePlayerRequest, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/players/${playerId}`,
				method: 'PUT',
				body: payload,
				...params
			})
	};
	teams = {
		/**
		 * No description
		 *
		 * @tags Teams
		 * @name GetTeams
		 * @summary Returns list of all the teams whose names contain the given query
		 * @request GET:/teams
		 */
		getTeams: (params: RequestParams = {}) =>
			this.request<TeamModel[], any>({
				path: `/teams`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name PostTeams
		 * @summary Creates a new team
		 * @request POST:/teams
		 */
		postTeams: (payload: CreateTeamRequest, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/teams`,
				method: 'POST',
				body: payload,
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name GetTeamById
		 * @summary Returns the team with the specified ID
		 * @request GET:/teams/{team_id}
		 */
		getTeamById: (teamId: number, params: RequestParams = {}) =>
			this.request<TeamModel, void>({
				path: `/teams/${teamId}`,
				method: 'GET',
				format: 'json',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name DeleteTeamById
		 * @summary Deletes the team with the specified ID
		 * @request DELETE:/teams/{team_id}
		 */
		deleteTeamById: (teamId: number, params: RequestParams = {}) =>
			this.request<void, any>({
				path: `/teams/${teamId}`,
				method: 'DELETE',
				...params
			}),

		/**
		 * No description
		 *
		 * @tags Teams
		 * @name PutTeamById
		 * @summary Updates league's data
		 * @request PUT:/teams/{team_id}
		 */
		putTeamById: (teamId: number, payload: CreateTeamRequest, params: RequestParams = {}) =>
			this.request<void, void>({
				path: `/teams/${teamId}`,
				method: 'PUT',
				body: payload,
				...params
			})
	};
}
