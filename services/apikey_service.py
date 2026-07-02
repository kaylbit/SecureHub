from repositories.api_key_repository import ApiKeyRepository
import secrets

class ApiKeyService:
  @staticmethod
  def generate_key():
    return secrets.token_urlsafe(32)

  @staticmethod
  def create(user_id, name):
    key = ApiKeyService.generate_key()
    ApiKeyRepository.create(user_id, key, name)
    return key
  
  @staticmethod
  def delete_key(key_id):
    return ApiKeyRepository.delete_key(key_id)
    
  @staticmethod
  def find_key(key_id):
    return ApiKeyRepository.find_by_key(key_id)
  
  @staticmethod
  def find_by_id(id):
    return ApiKeyRepository.find_by_id(id)
  
  @staticmethod
  def get_user_keys(api_key):
    return ApiKeyRepository.get_user_keys(api_key)

  