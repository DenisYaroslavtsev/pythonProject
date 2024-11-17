from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users/")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="UrbanUsers")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter Age", example="29")]):
    max_id = str(max(map(int, users.keys()), default=0) + 1)
    users[max_id] = f'Имя: {username}, возраст: {age}'
    return f'User {max_id} is registered'


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[str, Path(min_length=1, max_length=99, description="Enter User ID", example="2")],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="UrbanUsers")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter Age", example="29")]):
    users[user_id] = f'Имя {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[str, Path(min_length=1, max_length=99, description="Enter User ID", example="2")]):
    users.pop(user_id)
    return f'User {user_id} has been delete'

