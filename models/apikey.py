class ApiKey:
  def __init__(self, id, user_id, api_key, name, created_at):
    self.id = id
    self.user_id = user_id
    self.api_key = api_key
    self.name = name
    self.created_at = created_at

  def to_dict(self):
    return {
        "id": self.id,
        "user_id": self.user_id,
        "name": self.name,
        "created_at": self.created_at
    }
  
  