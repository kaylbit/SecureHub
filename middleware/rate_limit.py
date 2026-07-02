from functools import wraps
from flask import jsonify, request
from services.rate_limit_service import RateLimitService

def rate_limit():
  def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
      ip = request.remote_addr
      endpoint = request.path

      if not RateLimitService.allowed(ip, endpoint):
        return jsonify({
          "error": "too many request"
        }), 429
      
      return f(*args, **kwargs)
    
    return wrapper
  
  return decorator
