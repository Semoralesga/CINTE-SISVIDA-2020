import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpErrorResponse,
  HttpHeaders,
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

import { CyclingTeam } from '../models/cycling-team.model';
import { API_URL } from '../env';

@Injectable({
  providedIn: 'root',
})
export class ApiClientService {
  USER = 'sebas';
  PASS = 'Sebas';
  constructor(private http: HttpClient) {}

  getTeams(): Observable<CyclingTeam[]> {
    return this.http.get<CyclingTeam[]>(`${API_URL}/cycling_teams`).pipe(
      catchError((error) => {
        console.log('>> Error', error);
        let errorMsg: string;
        if (error.error instanceof ErrorEvent) {
          errorMsg = `Error: ${error.error.message}`;
        } else {
          errorMsg = this.getServerErrorMessage(error);
        }

        return throwError(errorMsg);
      })
    );
  }

  createTeam(data: CyclingTeam): Observable<CyclingTeam> {
    console.log('>>Data', data);
    return this.http
      .post<CyclingTeam>(`${API_URL}/cycling_teams/new`, data)
      .pipe(
        catchError((error) => {
          console.log('>> Error', error);
          let errorMsg: string;
          if (error.error instanceof ErrorEvent) {
            errorMsg = `Error: ${error.error.message}`;
          } else {
            errorMsg = this.getServerErrorMessage(error);
          }

          return throwError(errorMsg);
        })
      );
  }

  editTeam(teamId: number, data: CyclingTeam): Observable<CyclingTeam> {
    return this.http
      .put<CyclingTeam>(`${API_URL}/cycling_teams/${teamId}/edit`, data)
      .pipe(
        catchError((error) => {
          console.log('>> Error', error);
          let errorMsg: string;
          if (error.error instanceof ErrorEvent) {
            errorMsg = `Error: ${error.error.message}`;
          } else {
            errorMsg = this.getServerErrorMessage(error);
          }

          return throwError(errorMsg);
        })
      );
  }

  deleteTeam(teamId: number): Observable<CyclingTeam> {
    console.log('>> DELETE REQUEST');
    return this.http
      .delete<CyclingTeam>(`${API_URL}/cycling_teams/${teamId}/delete`)
      .pipe(
        catchError((error) => {
          console.log('>> Error', error);
          let errorMsg: string;
          if (error.error instanceof ErrorEvent) {
            errorMsg = `Error: ${error.error.message}`;
          } else {
            errorMsg = this.getServerErrorMessage(error);
          }

          return throwError(errorMsg);
        })
      );
  }
  private getServerErrorMessage(error: HttpErrorResponse): string {
    switch (error.status) {
      case 404: {
        return `Not Found: ${error.message}`;
      }
      case 403: {
        return `Access Denied: ${error.message}`;
      }
      case 500: {
        return `Internal Server Error: ${error.message}`;
      }
      default: {
        return `Unknown Server Error: ${error.message}`;
      }
    }
  }
}
