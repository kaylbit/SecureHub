from werkzeug.security import check_password_hash
from database.db import DbConnect
from flask import *

class User:
  def __init__(self, id, username, password, role, failed_attempts, locked_until):
    self.id = id
    self.username = username
    self.password = password
    self.role = role
    self.failed_attempts = failed_attempts
    self.locked_until = locked_until
  
  def to_dict(self):
    return {
        "id": self.id,
        "username": self.username,
        "role": self.role,
        "failed_attempts": self.failed_attempts,
        "locked_until": self.locked_until
    }

  def verify_pass(self, password): 
    return check_password_hash(self.password, password)

    

        