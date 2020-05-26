import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";

import { environment } from "@environments/environment";
import { Task } from "@app/_models";

@Injectable({ providedIn: "root" })
export class TaskService {
  constructor(private http: HttpClient) {}

  getAll() {
    return this.http.get<Task[]>(`${environment.apiUrl}/todos/todos`);
  }

  getById(id: number) {
    return this.http.get<Task>(`${environment.apiUrl}/todos/todos/${id}`);
  }

  post(text: string) {
    if (text.trim().length > 0)
      return this.http.post<Task>(`${environment.apiUrl}/todos/todos`, {text});
  }

  put(id: number, values: {}){
    return this.http.put<Task>(`${environment.apiUrl}/todos/todos/${id}`, values);
  }

  delete(id: number) {
    return this.http.delete(`${environment.apiUrl}/todos/todos/${id}`);
  }
}
