import os
from dotenv import load_dotenv

load_dotenv()  # read .env file

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
