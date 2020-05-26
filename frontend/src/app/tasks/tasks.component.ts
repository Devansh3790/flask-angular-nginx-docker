import { Component, OnInit } from "@angular/core";
import { first } from "rxjs/operators";

import { TaskService } from "@app/_services";
import { Task } from "@app/_models";

@Component({
  selector: "app-todos",
  templateUrl: "./tasks.component.html",
  styleUrls: ["./tasks.component.css"],
})
export class TasksComponent implements OnInit {
  public tasks: Task[] = [];
  public todoItemText: string = "";

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.loadAllTodoList();
  }

  loadAllTodoList() {
    this.taskService.getAll().subscribe((tasks) => {
      this.tasks = tasks;
    });
  }

  onClickTodoDelete(id) {
    this.taskService
      .delete(id)
      .pipe(first())
      .subscribe(() => {
        this.tasks = this.tasks.filter((x) => x.id !== id);
      });
  }

  onTaskAdd(event) {
    let text = event.target.value;
    event.target.value = '';
    this.taskService.post(text).subscribe((newTask: Task) => {
      this.todoItemText = "";
      this.tasks.push(newTask);
    });
  }

  updateTodoById(id: number, values: Object = {}) {
    this.taskService.put(id, values).subscribe();
  }

  // Toggle todo complete
  toggleTodoComplete(todo: Task) {
    todo.completed = !todo.completed;
    this.updateTodoById(todo.id, { completed: todo.completed });
  }
}
