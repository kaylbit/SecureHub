from functools import wraps
from middleware.auth import *
from flask import *

def require_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if g.token["type"] != "access":
            return jsonify({
                "error": "Invalid token"
            }), 401
        
        return f(*args, **kwargs)
    
    return decorated