from database.db import DbConnect

class RateLimitRepository:
  @staticmethod
  def find(ip, endpoint):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
      SELECT * FROM rate_limits WHERE ip=? AND endpoint=?
    """, (ip, endpoint))

    result = cursor.fetchone()

    conn.close()

    return result
  
  @staticmethod
  def create(ip, endpoint, reques_count, window_start):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
      INSERT INTO rate_limits(ip, endpoint, request_count, window_start)
      VALUES(?, ?, ?, ?)
    """, (ip, endpoint, reques_count, window_start))

    conn.commit()
    conn.close()

  @staticmethod
  def update_count(ip, endpoint, count, window_start):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
      UPDATE rate_limits SET request_count=?, window_start=? 
      WHERE ip=? AND endpoint=?
    """, (count, window_start, ip, endpoint))

    conn.commit()
    conn.close()

  