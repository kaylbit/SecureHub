from functools import wraps
from flask import request, jsonify, g
from configuration.config import *
from repositories.user_repository import *
import jwt

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth:
            return jsonify({
                "error": "Missing token"
            }), 401
        
        try:
            token = auth.split(" ")[1]

            decoded = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[JWT_ALGORITHM]
            )

            user = UserRepository.find_user(decoded["username"])
            g.token = decoded
            g.user = user

        except jwt.ExpiredSignatureError:
            return jsonify({
                "error": "Token expired"
            }), 401

        except jwt.InvalidTokenError:
            return jsonify({
                "error": "Invalid token"
            }), 401
        
        return f(*args, **kwargs)
    
    return decorated








