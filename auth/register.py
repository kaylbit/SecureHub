from services.user_service import UserService
from services.audit_service import AuditService
from werkzeug.security import generate_password_hash, check_password_hash
from flask import *

register_api = Blueprint("register_api", __name__)

@register_api.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
        "error": "Username and password are required"
      }), 400
    
    if len(password) < 8:
        return jsonify({
        "error": "Password must be at least 8 characters long"
      }), 400
    
    result = UserService.register_user(username, password)

    if not result == True:
        return jsonify({"error": "Username already exists"}), 400
    
    AuditService.create_log(username, "Register", "/auth/register")

    return jsonify({
        "success": "Registered successfully"
    }), 201


