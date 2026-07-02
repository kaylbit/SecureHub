from repositories.post_repository import PostRepository
from flask import *

class PostService:
  @staticmethod
  def find_by_id(id):
    post = PostRepository.find_by_id(id)
    return post

  @staticmethod
  def delete_post(post_id):
    PostRepository.delete_post(post_id)

    return True

  @staticmethod
  def update_post(post_id, title, content):
    result = PostRepository.update_post(
          post_id,
          title,
          content
      )


  @staticmethod
  def create_post(user_id, title, content):
     PostRepository.create_post(user_id, title, content)

  @staticmethod
  def get_post():
     return PostRepository.get_post()
     
  
