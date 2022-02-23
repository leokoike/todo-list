from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.route.todo_route import app as todo_app

app = FastAPI(title="TODO LIST API", description="Todo list API.", version="1.1.0-1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(todo_app, prefix="/api", tags=["TODO"])
