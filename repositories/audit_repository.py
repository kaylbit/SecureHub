from database.db import *

class AuditRepository:
  @staticmethod
  def create_log(username, action, endpoit):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
      INSERT INTO audit_logs(username, action, endpoint) VALUES(?, ?, ?)
    """, (username, action, endpoit))

    conn.commit()
    conn.close()

  @staticmethod
  def get_logs():
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT * FROM audit_logs ORDER BY id DESC
    """)

    logs = cursor.fetchall()

    conn.commit()
    conn.close()

    return logs
