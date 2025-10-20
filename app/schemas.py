from pydantic import BaseModel, EmailStr, Field, constr
from typing import Optional , Annotated
import re

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


class UserCreate(BaseModel):
    username: str
    email: str
    role: Optional[str] = "Member"
    password: Annotated[
        str,
        Field(
            min_length=8,
            pattern=re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$"),
            description="Password must contain at least one uppercase, one lowercase, and one number",
        ),
    ]


class UserOut(BaseModel):
    id:int
    email:str
    role:str
    is_active:bool


    class Config:
        from_attributes=True
    
