from services.user_service import UserService
from services.audit_service import AuditService
from database.db import DbConnect
from werkzeug.security import generate_password_hash, check_password_hash
from services.auth_service import AuthService
from middleware.rate_limit import rate_limit
from flask import *
import time 

auth_login = Blueprint("login", __name__)

@auth_login.route("/auth/login", methods=["POST"])
@rate_limit()
def login():
  if request.method == "POST":
    data = request.get_json()

    if not data:
      return jsonify({
          "error": "Missing JSON body"
      }), 400

    username = data.get("username")
    password = data.get("password")

    user = UserService.find_user(username)

    if not user:
      return jsonify({
          "error": "Invalid credentials"
      }), 401
    
    current_time = int(time.time())

    if user.locked_until > current_time:
      return jsonify({
        "error": "Account temporarily locked"
      }), 403
    
    if user.locked_until > 0 and user.locked_until <= current_time:
      UserService.reset_failed_attempts(user.id)
      user.failed_attempts = 0

    if user.failed_attempts >= 5:
      AuditService.create_log(username, "LOCKED_ACCOUNT", "/auth/login")
      return jsonify({
        "error": "Account locked. Please try again later"
      }), 403
    
    if user.verify_pass(password):
      access_token = AuthService.generate_access(user)
      refresh_token = AuthService.generate_refresh(user)
      
      conn = DbConnect.db()
      cursor = conn.cursor()
      cursor.execute("""
        INSERT INTO refresh_tokens(username, token) VALUES(?,?)            
      """, (user.username, refresh_token))
      
      conn.commit()
      conn.close()
      
      AuditService.create_log(username, "LOGIN", "/auth/login")

      return jsonify({
          "access_token": access_token,
          "refresh_token": refresh_token
      }), 200
    
    new_attempt = user.failed_attempts + 1
    UserService.increment_failed_attempts(user.id)
    AuditService.create_log(username, "FAILED_LOGIN", "/auth/login")

    if new_attempt >= 5:
      UserService.lock_account(user.id, current_time + 60)
      AuditService.create_log(username, "LOCKED_ACCOUNT", "/auth/login")
      return jsonify({""
        "error": "Account locked due to too many failed attempts"
      }), 403
    
    return jsonify({"error": "Invalid credentials"}), 401

    



    
        

        
    
            
        




