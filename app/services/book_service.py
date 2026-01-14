from app.api.client import fetch_books
from app.database.models import create_table, insert_books, fetch_all_books

def run_pipeline():
    print("Initializing database...")
    create_table()

    print("Fetching books from API...")
    books = fetch_books()

    print("Saving books to database...")
    insert_books(books)

    print("Books stored:\n")
    for title, author, year in fetch_all_books():
        print(f"{title} | {author} | {year}")
