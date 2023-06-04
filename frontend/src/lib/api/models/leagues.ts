import type { BaseModel } from './baseModel';
import type { Team } from './team';

export interface League extends BaseModel {
	name: string;
	teams: Team[];
}

// api

export interface CreateLeagueRequest {
	name: string;
}
