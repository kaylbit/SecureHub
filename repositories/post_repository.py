from database.db import *
from flask import *
from models.post import Post

class PostRepository:
  @staticmethod
  def find_by_id(post_id):
    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM posts WHERE id=?
        """,(post_id,))

    post = cursor.fetchone()
    conn.close()

    if post:
      return Post(
        post["id"],
        post["user_id"],
        post["title"],
        post["content"]
      )
    
    return False

  @staticmethod
  def create_post(user_id, title, content):
    conn = DbConnect.db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO posts(user_id, title, content) VALUES (?,?,?)
    """,(user_id, title, content))
    conn.commit()
    conn.close()
    
    return jsonify({
        "success": True
      }), 200
  
  @staticmethod
  def get_post():
    conn = DbConnect.db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM posts
    """)
    posts = cursor.fetchall()

    conn.commit()
    conn.close()

    result = [dict(post) for post in posts]
    return result
  
  @staticmethod
  def delete_post(post_id):
    try:
      conn = DbConnect.db()
      cursor = conn.cursor()
      cursor.execute("""
          DELETE FROM posts WHERE id=?
      """, (post_id,))
      conn.commit()
      conn.close()

    except Exception as e:
      return f"error {e}"
    
  @staticmethod
  def update_post(post_id, title, content):
      conn = DbConnect.db()
      cursor = conn.cursor()

      cursor.execute("""
          UPDATE posts SET title=?, content=? WHERE id=?
      """, (title, content, post_id))
      
      conn.commit()
      conn.close()