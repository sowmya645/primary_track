from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Task Model
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

tasks: List[Task] = []
next_id = 1

# Get all tasks
@app.get("/api/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Get single task
@app.get("/api/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Create new task
@app.post("/api/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    if not task.title:
        raise HTTPException(status_code=400, detail="Title is required")

    # Prevent duplicate IDs
    if any(t.id == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Duplicate ID")

    tasks.append(task)
    return task

# Update task
@app.put("/api/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            if not isinstance(updated_task.completed, bool):
                raise HTTPException(status_code=400, detail="Completed must be boolean")
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete task
@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")