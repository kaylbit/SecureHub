from flask import *
from middleware.auth import *
from middleware.token import *
from services.post_service import *
from services.audit_service import *

post_api = Blueprint("post_api", __name__)

@post_api.route("/api/posts", methods=["POST"])
@require_auth
@require_token
def create_post():
    data = request.get_json()

    title = data.get("title")
    content = data.get("content")

    PostService.create_post(
      g.user.id,
      title,
      content
    )

    AuditService.create_log(g.user.id, "CREATE POST", "/api/posts")
    return jsonify({
        "message": "Post created"
    }), 201
    
@post_api.route("/api/posts", methods=["GET"])
@require_auth
@require_token
def get_post():
    posts = PostService.get_post()
    
    return jsonify(posts), 200


@post_api.route("/api/posts/<int:post_id>", methods=["DELETE"])
@require_auth
@require_token
def delete_post(post_id):
    check_post = PostService.find_by_id(post_id)

    if check_post.user_id == g.user.id:
        PostService.delete_post(post_id)
        AuditService.create_log(g.user.id, "DELETE POST", f"/api/posts/{post_id}")

        return jsonify({
            "message": "Post deleted"
        })
    
    return jsonify({
        "error": "Forbidden"
    }), 403

@post_api.route("/api/posts/<int:post_id>", methods=["PUT"])
@require_auth
@require_token
def update_post(post_id):
    post = PostService.find_by_id(post_id)

    if not post:
        return jsonify({
            "error": "Not found"
        }), 404

    if post.user_id == g.user.id:
        data = request.get_json()

        PostService.update_post(
            post_id, 
            data.get("title"),
            data.get("content")
        )

        AuditService.create_log(g.user.id, "UPDATE POST", f"/api/posts/{post_id}")
        return jsonify({
            "message": "Updated"
        })
    
    return jsonify({
        "error": "Forbidden"
    }), 403
    
