from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(
    docs_url=None,  # disable default docs
    redoc_url=None,
    openapi_url="/openapi.json",
)


# Create API router
api_router = APIRouter()

# CORS (keep it open for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory DB
todos = []

# -------- ROUTES -------- #
@app.get("/docs", include_in_schema=False)
def custom_docs():
    # Relative URL: resolves to /openapi.json for /docs and /api/openapi.json for /api/docs (e.g. behind ingress)
    return get_swagger_ui_html(
        openapi_url="openapi.json",
        title="API Docs",
    )

@api_router.get("/health")
def health():
    return {"status": "ok"}

@api_router.get("/")
def read_root():
    return {"message": "Todo API is running"}

@api_router.post("/todos")
def add_todo(task: str):
    todo = {"id": len(todos) + 1, "task": task}
    todos.append(todo)
    return todo

@api_router.get("/todos")
def get_todos():
    return todos

@api_router.put("/todos/{todo_id}")
def update_todo(todo_id: int, task: str):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["task"] = task
            return todo
    return {"error": "Todo not found"}

@api_router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"message": "Deleted"}

app.include_router(api_router)