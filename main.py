from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

todos = []
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")

@app.get("/")
def read_root():
    return {"message": "Todo API is running"}

@app.post("/todos")
def add_todo(task: str):
    todo = {"id": len(todos) + 1, "task": task}
    todos.append(todo)
    return todo

@app.get("/todos")
def get_todos():
    return todos

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, task: str):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["task"] = task
            return todo
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"message": "Deleted"}