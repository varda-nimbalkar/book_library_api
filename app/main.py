# app/main.py

from fastapi import FastAPI
from app.database import engine, Base
from app.routes import books , users
import uvicorn
from app import models

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Book Library API",
    description="A backend API to manage a digital book library",
    version="1.0.0"
)

# Include book routes
app.include_router(books.router)
app.include_router(users.router)

# Root route
@app.get("/")
def read_root():
    return 

# For local development
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
