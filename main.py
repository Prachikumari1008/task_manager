from fastapi import FastAPI, HTTPException, Query
from typing import List
from models import Task
from schemas import TaskCreate, TaskOut

app = FastAPI(title="Unix-Inspired Task Manager API ")

# Store tasks in-memory
tasks: List[Task] = []

@app.get("/tasks", response_model=List[TaskOut])
def list_tasks():
    return tasks

@app.post("/tasks", response_model=TaskOut)
def create_task(task_data: TaskCreate):
    task = Task(task_data.name)
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    global tasks
    updated_tasks = [task for task in tasks if task.id != task_id]
    if len(updated_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[:] = updated_tasks
    return

@app.patch("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, status: str = Query(..., example="completed")):
    for task in tasks:
        if task.id == task_id:
            task.status = status
            return task
    raise HTTPException(status_code=404, detail="Task not found")
