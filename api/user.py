from services.user_service import UserService 
from flask import Blueprint, request, jsonify
from services.audit_service import AuditService
from middleware.auth import * 

user_api = Blueprint("user_api", __name__)

@user_api.route("/api/users/<int:user_id>")
@require_auth
def user(user_id):
    if g.user.id != user_id:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    user = UserService.check_user(user_id)
    
    if not user:
        return jsonify({
            "error": "Invalid user"
        }), 401
    
    AuditService.create_log(g.user.id, "GET_USER", f"/api/users/{user_id}")
    return jsonify({
        "id": user.id,
        "username": user.username,
        "role": user.role
    }) 

@user_api.route("/api/users/<int:user_id>", methods=["PUT"])
@require_auth
def update_user(user_id):
    try:
      if g.user.id !=  user_id:
          return jsonify({
            "error": "Forbidden"
        }), 403

      data = request.get_json()

      username = data.get("username")

      if "username" not in data:
         return jsonify({
            "error": "Unprocessable Content"
         }), 422 

      UserService.update_user(
          user_id,
          username
      )

      AuditService.create_log(g.user.id, "UPDATE_USER", f"/api/users/{user_id}")
      
      return jsonify({
          "message": "User updated"
      })
    
    except jwt.ExpiredSignatureError:
      return jsonify({
          "error": "Token expired"
      }), 401

    except jwt.InvalidTokenError:
      return jsonify({
              "error": "Invalid token"
          }), 401
    
    



