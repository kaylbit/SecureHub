from repositories.rate_limit_repository import RateLimitRepository
import time

class RateLimitService:
  window = 180
  max_request = 5

  @staticmethod
  def find(ip, endpoint):
    return RateLimitRepository.find(ip, endpoint)
  
  @staticmethod
  def allowed(ip, endpoint):
    current_time = int(time.time())
    record = RateLimitRepository.find(ip, endpoint)

    if not record:
      RateLimitRepository.create(ip, endpoint, 1, current_time)
      return True

    count = record["request_count"]
    window_start = record["window_start"]

    if current_time - window_start > 60:
      RateLimitRepository.update_count(ip, endpoint, 1, current_time)
      return True
    
    if count >= 5:
      return False
    
    RateLimitRepository.update_count(ip, endpoint, count + 1, window_start)
    return True

