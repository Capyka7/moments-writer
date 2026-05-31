"""
Storage — save and manage favorite Moments copy (SQLite).
"""

import json
import sqlite3
import os
from datetime import datetime
from pathlib import Path

DB_PATH = Path.home() / ".moments-writer.db"


def get_conn():
    """Get database connection."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    _init_db(conn)
    return conn


def _init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            tags TEXT DEFAULT '',
            style TEXT DEFAULT 'casual',
            topic TEXT DEFAULT '',
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.commit()


def save_favorite(text, tags="", style="casual", topic=""):
    """Save a copy to favorites."""
    conn = get_conn()
    conn.execute(
        "INSERT INTO favorites (text, tags, style, topic) VALUES (?, ?, ?, ?)",
        (text, tags, style, topic),
    )
    conn.commit()
    conn.close()
    return True


def get_favorites(limit=50, offset=0):
    """Get saved favorites."""
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM favorites ORDER BY created_at DESC LIMIT ? OFFSET ?",
        (limit, offset),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_favorite(fav_id):
    """Delete a favorite."""
    conn = get_conn()
    conn.execute("DELETE FROM favorites WHERE id = ?", (fav_id,))
    conn.commit()
    conn.close()


def search_favorites(keyword):
    """Search favorites by keyword."""
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM favorites WHERE text LIKE ? OR tags LIKE ? ORDER BY created_at DESC",
        (f"%{keyword}%", f"%{keyword}%"),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
