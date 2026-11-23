import sqlite3
DB_NAME = "cards.db"
def connect():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                card_set TEXT NOT NULL,
                rarity TEXT NOT NULL,
            number TEXT NOT NULL,
            artist TEXT NOT NULL
        )
    """)
def add_card(name, card_set, rarity, number, artist):
    with connect() as conn:
        cursor = conn.execute("""
            INSERT INTO cards (name, card_set, rarity, number, artist)
            VALUES (?, ?, ?, ?, ?)
        """, (name, card_set, rarity, number, artist))
        return cursor.lastrowid
def get_all_cards():
    with connect() as conn:
        rows = conn.execute("SELECT * FROM cards").fetchall()
        return [dict(row) for row in rows]
def find_cards_by_set(card_set):
    with connect() as conn:
        rows = conn.execute("SELECT * FROM cards WHERE card_set = ?", (card_set,)).fetchall()
        return [dict(row) for row in rows]
def delete_card(card_id):
    with connect() as conn:
        cursor = conn.execute("DELETE FROM cards WHERE id = ?", (card_id,))
        return cursor.rowcount > 0
def get_rarity_report():
    with connect() as conn:
        rows = conn.execute("""
            SELECT rarity, COUNT(*) AS count
            FROM cards
            GROUP BY rarity
            ORDER BY rarity
        """).fetchall()
        return [dict(row) for row in rows]