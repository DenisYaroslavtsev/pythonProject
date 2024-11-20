from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def home_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="UrbanUsers")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter Age", example="29")]) -> User:
    new_id = max([user.id for user in users], default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, description="Enter User ID", example="2")],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="UrbanUsers")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter Age", example="29")]) -> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, description="Enter User ID", example="2")]) -> User:
    try:
        for index, user in enumerate(users):
            if user.id == user_id:
                return users.pop(index)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
