from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://mongodb-service:27017/")
db = client["todo_db"]
collection = db["todos"]

app = FastAPI(
    docs_url="/api/docs",   # disable default docs
    redoc_url=None,
    openapi_url="/api/openapi.json",
)

# CORS (keep open for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------- MODELS -------- #
class Todo(BaseModel):
    task: str

# -------- ROUTER -------- #
api_router = APIRouter(prefix="/api")

# In-memory DB
#todos = []

# -------- CUSTOM DOCS -------- #
@app.get("/docs", include_in_schema=False)
def custom_docs():
    return get_swagger_ui_html(
        openapi_url="/api/openapi.json",
        title="API Docs",
        swagger_ui_parameters={
            "url": "/api/openapi.json"
        },
    )

# -------- ROUTES -------- #
@api_router.get("/health")
def health():
    return {"status": "ok"}

@api_router.get("/")
def read_root():
    return {"message": "Todo API is running"}

@api_router.post("/todos")
def add_todo(data: dict):
    task = data.get("task")
    result = collection.insert_one({"task": task})
    return {"id": str(result.inserted_id), "task": task}

@api_router.get("/todos")
def get_todos():
    todos = []
    for item in collection.find():
        todos.append({
            "id": str(item["_id"]),
            "task": item["task"]
        })
    return todos

@api_router.put("/todos/{todo_id}")
def update_todo(todo_id: str, data: dict):
    task = data.get("task")
    collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": {"task": task}}
    )
    return {"id": todo_id, "task": task}

@api_router.delete("/todos/{todo_id}")
def delete_todo(todo_id: str):
    collection.delete_one({"_id": ObjectId(todo_id)})
    return {"message": "Deleted"}

# Include router
app.include_router(api_router)