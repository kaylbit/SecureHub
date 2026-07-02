from flask import *
from middleware.apikey_auth import api_key_auth

service_profile_api = Blueprint("service_profile_api", __name__)

@service_profile_api.route("/api/service/profile", methods=["GET"])
@api_key_auth()
def service_profile():
  return jsonify({
    "id": g.user.id,
    "username": g.user.username,
    "role": g.user.role
  })
