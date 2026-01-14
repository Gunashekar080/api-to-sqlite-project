from app.database.connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_books(books):
    conn = get_connection()
    cursor = conn.cursor()
    for book in books:
        cursor.execute("""
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        """, (
            book.get("title"),
            book.get("author"),
            book.get("publication_year")
        ))
    conn.commit()
    conn.close()

def fetch_all_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, publication_year FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows
