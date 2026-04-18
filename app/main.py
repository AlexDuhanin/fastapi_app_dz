from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api import api_router
import os

app = FastAPI(title="My Website")

# Правильный путь к статическим файлам
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализация шаблонов — путь должен указывать на папку templates в корне проекта
templates = Jinja2Templates(directory="templates")

# Подключение API роутера
app.include_router(api_router, prefix="/api")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about/")
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "site_name": "Сайт с книгами",
            "developer": "Алексей Духанин",
            "description": "На этом сайте я выкладываю мои любимые книги"
        }
    )
