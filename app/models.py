from sqlalchemy import Column, Integer, String, Boolean , ForeignKey , Text , DateTime # type: ignore
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    page_count = Column(Integer, nullable=False)
    publication_year = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    is_available = Column(Boolean, default=True)

    #Foreign keys

    author_id = Column(Integer,ForeignKey("authors.id",ondelete="CASCADE"))
    added_by_id = Column(Integer,ForeignKey("users.id",ondelete="SET NULL"),nullable=True)

    ## Relationships

    author = relationship("Author",back_populates="books")
    added_by = relationship("User",back_populates="books")
    reviews = relationship("Review",back_populates="book",cascade="all,delete")



class Review(Base):
    __tablename__ = "reviews"

    id=Column(Integer,primary_key=True,index=True)
    rating = Column(Integer , nullable=False)
    comment = Column(Text , nullable=True)
    created_at = Column(DateTime , default=datetime.utcnow)

    # Foreign keys  
    user_id = Column(Integer , ForeignKey("users.id",ondelete="CASCADE"))
    book_id = Column(Integer , ForeignKey("books.id",ondelete="CASCADE"))

    # Relationships

    user = relationship("User" , back_populates="reviews")
    book = relationship("Book",back_populates="reviews")
        
class User(Base):
    __tablename__ = "users"

    id=Column(Integer , primary_key = True , index = True)
    email=Column(String , unique=True , nullable = False , index=True)
    hashed_password =Column(String , nullable=False)
    role = Column(String , default="Member")
    is_active = Column(Boolean , default=True)

    ## Relationship

    reviews = relationship("Review",back_populates="user",cascade="all,delete")
    books=relationship("Book",back_populates="added_by",cascade="all,delete")



class Author(Base):
    __tablename__="authors"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    biography=Column(Text,nullable=True)

    books=relationship("Book",back_populates="author",cascade="all,delete")





    
