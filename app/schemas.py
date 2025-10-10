from pydantic import BaseModel, Field
from typing import Optional

# Schema for creating a book
class BookCreate(BaseModel):
    title: str = Field()
    author: str = Field()
    genre: str = Field()
    page_count: int = Field()
    publication_year: int = Field()
    description: Optional[str] = Field()
    is_available: Optional[bool] = True  


# Schema for updating a book
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    page_count: Optional[int] = None
    publication_year: Optional[int] = None
    description: Optional[str] = None
    is_available: Optional[bool] = None


# Schema for reading a book (response)

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    page_count: int
    publication_year: int
    description: Optional[str]
    is_available: bool

    class Config:
        from_attributes = True
