from functools import wraps
from flask import request, jsonify
from configuration.config import *
from repositories.user_repository import *
import jwt
from middleware.auth import *

def require_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if g.user.role != "admin":
            return jsonify({
                "error": "Forbidden"
            }),403

        return f(*args, **kwargs)

    return decorated