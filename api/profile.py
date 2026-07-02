from flask import jsonify
from middleware.auth import *
from middleware.token import *
from services.audit_service import AuditService

profile_api = Blueprint("profile_api", __name__)

@profile_api.route("/api/profile", methods=["GET"])
@require_auth
@require_token
def profile():
    AuditService.create_log(g.user.id, "GET_PROFILE", "/api/profile")
    return jsonify(g.user.to_dict())


