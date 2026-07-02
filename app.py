from database.init_db import DatabaseInit
from auth.login import auth_login
from flask import *
from api.profile import profile_api
from api.admin import admin_api
from auth.register import register_api
from api.user import user_api
from api.posts import post_api
from api.api_key import key_api
from api.service import service_profile_api

class main:
    DatabaseInit.db_init()

    app = Flask(__name__)
    app.register_blueprint(auth_login)
    app.register_blueprint(profile_api)
    app.register_blueprint(admin_api)
    app.register_blueprint(register_api)
    app.register_blueprint(user_api)
    app.register_blueprint(post_api)
    app.register_blueprint(key_api)
    app.register_blueprint(service_profile_api)

    if __name__ == "__main__":
        app.run(debug=True)
