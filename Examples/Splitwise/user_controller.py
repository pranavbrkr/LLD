from typing import List, Optional
from user import User

class UserController:
  def __init__(self):
    self.user_list: List[User] = []
  
  def addUser(self, user: User):
    self.user_list.append(user)
  
  def getUser(self, user_id: str):
    for user in self.user_list:
      if user.getUserId() == user_id:
        return user
    return None
  
  def getAllUsers(self) -> List[User]:
    return self.user_list