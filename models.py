from db.database import connect_db

def add_asset(name, category, quantity, expiry_date, supplier):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO assets (name, category, quantity, expiry_date, supplier)
        VALUES (?, ?, ?, ?, ?)
    """, (name, category, quantity, expiry_date, supplier))
    conn.commit()
    conn.close()

def get_assets():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_asset(id, name, category, quantity, expiry_date, supplier):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE assets
        SET name = ?, category = ?, quantity = ?, expiry_date = ?, supplier = ?
        WHERE id = ?
    """, (name, category, quantity, expiry_date, supplier, id))
    conn.commit()
    conn.close()

def delete_asset(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assets WHERE id = ?", (id,))
    conn.commit()
    conn.close()
