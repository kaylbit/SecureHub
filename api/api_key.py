from flask import *
from middleware.auth import *
from middleware.token import *
from services.apikey_service import ApiKeyService

key_api = Blueprint("key_api", __name__)

@key_api.route("/api/key", methods=["POST"])
@require_auth
@require_token
def create():
  data = request.get_json()

  if not data:
    return jsonify({
      "error": "Missing JSON body"
    }), 400
  
  name = data.get("name")
  key = ApiKeyService.create(g.user.id, name)

  return jsonify({
    "api_key": key
  }), 201


@key_api.route("/api/key", methods=["GET"])
@require_auth
@require_token
def list_key():
  keys = ApiKeyService.get_user_keys(g.user.id)

  result = [dict(key) for key in keys]

  return jsonify(result)


@key_api.route("/api/key/<int:key_id>", methods=["DELETE"])
@require_auth
def delete_key(key_id):
  user = ApiKeyService.find_by_id(key_id)

  if user.user_id != g.user.id:
    return jsonify({
      "error": "Forbidden"
    }), 403

  ApiKeyService.delete_key(key_id)

  return jsonify({
    "success": "API key deleted"
  }), 201

  

