import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "memory.db"


def init_memory():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT,
            value TEXT,
            type TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_memory(key: str, value: str, mem_type: str = "fact"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO memory (key, value, type) VALUES (?, ?, ?)",
        (key.lower(), value, mem_type)
    )

    conn.commit()
    conn.close()


def get_memory(key: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "SELECT value FROM memory WHERE key = ? ORDER BY id DESC LIMIT 1",
        (key.lower(),)
    )

    row = cur.fetchone()
    conn.close()

    return row[0] if row else None


def list_memory(mem_type: str = "fact"):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "SELECT key, value FROM memory WHERE type = ?",
        (mem_type,)
    )

    rows = cur.fetchall()
    conn.close()
    return rows
