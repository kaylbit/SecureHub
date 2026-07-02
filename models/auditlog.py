class AuditLog:
  def __init__(self, username, action, endpoint):
    self.username = username
    self.action = action
    self.endpoint = endpoint