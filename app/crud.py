from sqlalchemy.orm import Session
from app import models, schemas

# Create a new book
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        genre=book.genre,
        page_count=book.page_count,
        publication_year=book.publication_year,
        description=book.description,
        is_available=book.is_available
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# Get  books with pagination
def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()



# Get a book by ID

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


# Update a book
def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return None
    for field, value in book.dict(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book


# Delete a book
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not db_book:
        return None
    db.delete(db_book)
    db.commit()
    return db_book


# Get books by author

def get_books_by_author(db: Session, author_name: str):
    return db.query(models.Book).filter(models.Book.author.ilike(f"%{author_name}%")).all()


# Search books by title or author
def search_books(db: Session, query: str):
    return db.query(models.Book).filter(
        or_(
            models.Book.title.ilike(f"%{query}%"),
            models.Book.author.ilike(f"%{query}%")
        )
    ).all()
