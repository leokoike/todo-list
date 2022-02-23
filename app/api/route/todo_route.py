from fastapi import APIRouter

app = APIRouter()


@app.get("/todo")
def get_all_todo():
    return {}
