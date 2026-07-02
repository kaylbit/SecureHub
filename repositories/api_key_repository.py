from database.db import DbConnect
from models.apikey import ApiKey

class ApiKeyRepository:
  @staticmethod
  def create(user_id, api_key, name):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
       INSERT INTO api_keys(user_id, api_key, name) VALUES(?,?,?)   
    """, (user_id, api_key, name))

    conn.commit()
    conn.close()

  @staticmethod
  def delete_key(key_id):
    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM api_keys WHERE id=?
    """, (key_id,))

    conn.commit()
    conn.close()


  @staticmethod
  def find_by_key(api_key):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
       SELECT * FROM api_keys WHERE api_key=?  
    """, (api_key,))

    result = cursor.fetchone()
    conn.close()

    if result:
      return ApiKey(
        result["id"],
        result["user_id"],
        result["api_key"],
        result["name"],
        result["created_at"]
      )

    return False
  
  @staticmethod
  def find_by_id(id):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
       SELECT * FROM api_keys WHERE id=?  
    """, (id,))

    result = cursor.fetchone()
    conn.close()

    if result:
      return ApiKey(
        result["id"],
        result["user_id"],
        result["api_key"],
        result["name"],
        result["created_at"]
      )

    return False 

  @staticmethod
  def get_user_keys(user_id):

    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM api_keys WHERE user_id=?
    """, (user_id,))

    keys = cursor.fetchall()


    conn.commit()
    conn.close()

    return keys
