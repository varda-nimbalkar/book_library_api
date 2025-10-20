Features
Create, Read, Update, Delete (CRUD) books

Search books by author or keywords

Track availability status of books

PostgreSQL as the database backend

Structured and validated data using Pydantic models


Tech Stack

Backend: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy

Python Version: 3.13+

Others: Pydantic, dotenv


### git clone <repository_url>
cd book_library_api

### Virtual Environment
python -m venv venv

### Activate the virtual environment
venv\Scripts\activate

### Create a .env file in the root directory

DATABASE_URL=postgresql://postgres:1234@localhost:5432/books

### Run the Application
uvicorn app.main:app --reload

### The API will be available at http://127.0.0.1:8000.
