# app/routes/books.py

from fastapi import APIRouter, Depends, Form, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas, database
from app.utils.logger import logger

# Create FastAPI router
router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create Book
@router.post("/", response_model=schemas.BookOut)
def create_book(
    title: str = Form(...),
    author: str = Form(...),
    genre: str = Form(...),
    page_count: int = Form(...),
    publication_year: int = Form(...),
    description: str = Form(...),
    is_available: bool = Form(...),
    db: Session = Depends(get_db)
):
    book_in = schemas.BookCreate(
        title=title,
        author=author,
        genre=genre,
        page_count=page_count,
        publication_year=publication_year,
        description=description,
        is_available=is_available
    )
    return crud.create_book(db, book_in)

# ✅ Get all books
@router.get("/", response_model=List[schemas.BookOut])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_books(db, skip=skip, limit=limit)

# ✅ Get book by ID
@router.get("/{book_id}", response_model=schemas.BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# ✅ Update a book
@router.put("/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book_update)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# ✅ Delete a book (no cover image check)
@router.delete("/{book_id}", response_model=schemas.BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# ✅ Get books by author
@router.get("/author/{author_name}", response_model=List[schemas.BookOut])
def get_books_by_author(author_name: str, db: Session = Depends(get_db)):
    return crud.get_books_by_author(db, author_name)

# ✅ Search books by title or author
@router.get("/search/", response_model=List[schemas.BookOut])
def search_books(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    return crud.search_books(db, q)
