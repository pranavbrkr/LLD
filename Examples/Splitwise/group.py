from typing import List
from expense import Expense
from expense_controller import ExpenseController
from expense_split_type import ExpenseSplitType
from split import Split
from user import User

class Group:
  def __init__(self):
    self.group_id: str = ""
    self.group_name: str = ""
    self.group_members: List[User] = []
    self.expense_list: List[Expense] = []
    self.expense_controller: ExpenseController = ExpenseController()

  def addMember(self, member: User):
    if member in self.group_members:
      print(f"User {member.getUserName()} is already a member of the group!")
    else:
      self.group_members.append(member)
      print(f"User {member.getUserName()} added to the group")

  def getGroupId(self) -> str:
    return self.group_id
  
  def setGroupId(self, group_id: str):
    self.group_id = group_id
  
  def setGroupName(self, group_name: str):
    self.group_name = group_name
  
  def getExpenses(self) -> List[Expense]:
    return self.expense_list
  
  def getGroupMembers(self) -> List[User]:
    return self.group_members
  
  def createExpense(self, expense_id: str, description: str, expense_amount: float, split_details: List[Split], split_type: ExpenseSplitType, paid_by_user: User) -> Expense:
    expense = self.expense_controller.createExpense(expense_id, description, expense_amount, split_details, split_type, paid_by_user)
    self.expense_list.append(expense)
    return expense