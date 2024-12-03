from fastapi import FastAPI
from app.routers import task, users

app = FastAPI()


@app.get('/')
def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(users.router)
