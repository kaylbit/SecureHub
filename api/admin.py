import jwt
from flask import jsonify
from services.user_service import UserService
from services.audit_service import AuditService
from middleware.auth import *
from middleware.admin import *

admin_api = Blueprint("admin_api", __name__)

@admin_api.route("/api/admin", methods=["GET"])
@require_auth
@require_admin
def admin():
    users = UserService.get_all_user()
    AuditService.create_log(g.user.id, "GET_USERS", "/api/admin")
    
    return jsonify(users)

@admin_api.route("/api/admin/logs", methods=["GET"])
@require_auth
@require_admin
def get_logs():
    AuditService.create_log(g.user.id, "GET_LOGS", "/api/admin/logs")
    logs = AuditService.get_logs()
    result = [dict(log) for log in logs]
    
    return jsonify(result)    
