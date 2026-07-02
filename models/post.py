class Post:
  def __init__(self, id, user_id, title, content):
    self.id = id
    self.user_id = user_id
    self.title = title
    self.content = content

  def to_dict(self):
    return {
        "id": self.id,
        "user_id": self.user_id,
        "title": self.title,
        "content": self.content
    }

  def is_owner(self, user_id):
    if self.id == user_id:
      return True
    
    return False
