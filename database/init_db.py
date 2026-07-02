import sqlite3
from database.db import DbConnect
from services.user_service import UserService

class DatabaseInit:
  def db_init():
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role text,
        failed_attempts INTEGER DEFAULT 0,
        locked_until INTEGER DEFAULT 0
    )
    """)
    admin = UserService.find_user("admin")

    if not admin:
      UserService.register_user("admin", "admin123", "admin")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS refresh_tokens(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        token text
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        content TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        action TEXT,
        endpoint TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rate_limits(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        endpoint TEXT,
        request_count INTEGER,
        window_start INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_keys(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        api_key TEXT,
        name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized")
