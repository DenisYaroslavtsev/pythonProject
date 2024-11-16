from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def home_page():
    return "Главная страница"


@app.get("/user/admin")
async def adm_panel():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def id_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]):
    return f'Вы вошли как пользователь №{user_id}'


@app.get("/user/{username}/{age}")
async def user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter Username", example="UrbanUser")],
        age: Annotated[int, Path(de=18, le=120, description="Enter Age", example="27")]):
    return f'Информация о пользователе. Имя: {username}, возраст: {age}'
