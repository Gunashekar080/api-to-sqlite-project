import requests
from app.config import API_URL

def fetch_books():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()
