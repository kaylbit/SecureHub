from repositories.audit_repository import AuditRepository 

class AuditService:
  @staticmethod
  def create_log(username, action, endpoint):
    return AuditRepository.create_log(username, action, endpoint)
  
  def get_logs():
    return AuditRepository.get_logs()