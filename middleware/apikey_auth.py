from functools import wraps
from flask import *
from services.apikey_service import ApiKeyService
from services.user_service import UserService

def api_key_auth():
  def decorator(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
      api_key = request.headers.get("X-API-Key")

      if not api_key:
        return jsonify({
          "error": "API key required"
        }), 401
      
      key = ApiKeyService.find_key(api_key)

      if not key:
        return jsonify({
          "error": "Invalid API key"
        })
      
      user = UserService.check_user(key.id)

      g.user = user

      return f(*args, **kwargs)
    
    return wrapper
  
  return decorator




