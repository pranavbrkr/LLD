from typing import List
from group import Group
from user import User

class GroupController:
  def __init__(self):
    self.group_list: List[Group] = []

  def createNewGroup(self, group_id: str, group_name: str, created_by_user: User) -> Group:
    group = Group()
    group.setGroupId(group_id)
    group.setGroupName(group_name)
    group.addMember(created_by_user)
    self.group_list.append(group)
    return group
  
  def getGroup(self, group_id: str):
    for group in self.group_list:
      if group.getGroupId() == group_id:
        return group
    print("No such group exists!")
    return None
  
  def getAllGroups(self) -> List[Group]:
    return self.group_list