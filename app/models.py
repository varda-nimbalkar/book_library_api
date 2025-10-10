from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

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
