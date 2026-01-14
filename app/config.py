import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
DB_PATH = os.getenv("DB_PATH", "data/books.db")
