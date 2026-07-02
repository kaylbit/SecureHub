from database.db import *
from models.users import User
from flask import *
from werkzeug.security import generate_password_hash, check_password_hash

class UserRepository:
  @staticmethod
  def find_user(username):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
       SELECT * FROM users WHERE username=?            
    """, (username,))
    is_user = cursor.fetchone()

    conn.close()

    if is_user:
      return User(
        is_user["id"],
        is_user["username"],
        is_user["password"],
        is_user["role"],
        is_user["failed_attempts"],
        is_user["locked_until"]
      )
    
    return False
  
  @staticmethod
  def check_user(id):
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
       SELECT * FROM users WHERE id=?            
    """, (id,))
    is_user = cursor.fetchone()

    conn.close()

    if is_user:
      return User(
        is_user["id"],
        is_user["username"],
        is_user["password"],
        is_user["role"],
        is_user["failed_attempts"],
        is_user["locked_until"]
      )
    
    return {"error": "Invalid does not exists"}
  
  @staticmethod
  def update_user(user_id, username):
    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET username=?
        WHERE id=?
    """,(username, user_id))

    conn.commit()
    conn.close()
 

  @staticmethod
  def register_user(username, password):
    uname = username
    pword = password

    pass_hash = generate_password_hash(pword)
 
    conn = DbConnect.db()
    cursor = conn.cursor()
    
    try:
      cursor.execute("""
        INSERT INTO users(username, password, role) VALUES(?,?,?)
      """, (uname, pass_hash, "user"))

      conn.commit()

      return jsonify({
        "success": True
      }), 200
    
    except sqlite3.IntegrityError:
      return jsonify({
        "success": False
      }), 401
    
    finally:
      conn.close()

    
  @staticmethod
  def get_all_users():
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    result = [dict(row) for row in users]

    return result
  
  @staticmethod
  def reset_failed_attempts(user_id):
    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET failed_attempts=0
        WHERE id=?
    """, (user_id,))

    conn.commit()
    conn.close()

  @staticmethod
  def increment_failed_attempts(user_id):
    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
      UPDATE users
      SET failed_attempts = failed_attempts + 1
      WHERE id=?
    """,(user_id,))

    conn.commit()
    conn.close()

  @staticmethod
  def lock_account(user_id, timestamp):
    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET locked_until=?
        WHERE id=?
    """, (timestamp, user_id))

    conn.commit()
    conn.close()


