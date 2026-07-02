import sqlite3
from configuration.config import DATABASE

DB_NAME = DATABASE

class DbConnect:
    @staticmethod
    def db():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn