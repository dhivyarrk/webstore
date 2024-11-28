import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from './models/user.model';
import { Observable } from 'rxjs';
import {API_URL} from './env';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  
  constructor(private http: HttpClient) { }

  signup(user: User): Observable<any> {
    console.log("user is", user);
    return this.http.post(`${API_URL}/signup`, user);
  }
  logout(): void {
    // Clear any stored authentication data (like tokens)
    localStorage.removeItem('token'); // Assuming token is stored in localStorage
    localStorage.removeItem('user_type'); // Assuming token is stored in localStorage
    sessionStorage.clear(); // Optionally clear session storage
  }
}
