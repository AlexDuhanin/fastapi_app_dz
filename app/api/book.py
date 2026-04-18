from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Модель данных для книги
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

# В памяти хранилище (для демонстрации)
books_db = [
    Book(id=1, title="1984", author="Джордж Оруэлл", year=1949),
    Book(id=2, title="451° по Фаренгейту", author="Рэй Брэдбери", year=1953),
]

# Роутер для книг
books_router = APIRouter(prefix="/books", tags=["books"])

@books_router.get("/", response_model=List[Book])
async def get_books():
    """Получить список всех книг"""
    return books_db

@books_router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Получить книгу по ID"""
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@books_router.post("/", response_model=Book)
async def create_book(book: Book):
    """Создать новую книгу"""
    books_db.append(book)
    return book

# Подключаем вложенный роутер
router.include_router(books_router)
