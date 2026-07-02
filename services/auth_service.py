from configuration.config import *
import datetime
import jwt

class AuthService:
  @staticmethod
  def generate_access(user):
    payload = {
      "id": user.id,
      "username": user.username,
      "role": user.role,
      "type": "access",
      "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=180)
    }

    return jwt.encode(
      payload,
      SECRET_KEY,
      algorithm=JWT_ALGORITHM
    )
  

  @staticmethod
  def generate_refresh(user):
    payload = {
      "id": user.id,
      "username": user.username,
      "role": user.role,
      "type": "refresh",
      "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=1440)
    }

    return jwt.encode(
      payload,
      SECRET_KEY,
      algorithm=JWT_ALGORITHM
    )
  
