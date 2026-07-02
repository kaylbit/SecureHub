from repositories.user_repository import UserRepository

class UserService:
  @staticmethod
  def find_user(username):
   return UserRepository.find_user(username)
  
  @staticmethod
  def check_user(id):
    return UserRepository.check_user(id)
  
  @staticmethod
  def update_user(user_id, username):
    return UserRepository.update_user(user_id, username)
  
  @staticmethod
  def register_user(username, password, role):
    return UserRepository.register_user(username, password, role)
  
  @staticmethod
  def get_all_user():
    users = UserRepository.get_all_users()
    return users
  
  @staticmethod
  def reset_failed_attempts(user_id):
    UserRepository.reset_failed_attempts(user_id)

  @staticmethod
  def increment_failed_attempts(user_id):
    UserRepository.increment_failed_attempts(user_id)

  @staticmethod
  def lock_account(user_id, timestamp):
    UserRepository.lock_account(user_id, timestamp)
