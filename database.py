import sqlite3

def connect_db():
    # Connect to the SQLite database
    conn = sqlite3.connect("pharmacy_assets.db")
    return conn

def initialize_db():
    # Initialize the database by creating the assets table if it doesn't exist
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER,
            expiry_date DATE,
            supplier TEXT
        )
    """)
    conn.commit()
    conn.close()
