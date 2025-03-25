from typing import List
from split import Split
from user import User
from expense_split_type import ExpenseSplitType

class Expense:
  def __init__(self, expense_id: str, expense_amount: float, description: str, paid_by_user: User, split_type: ExpenseSplitType, split_details: List[Split]):
    self.expense_id: str = expense_id
    self.expense_amount: float = expense_amount
    self.description: float = description
    self.paid_by_user: User = paid_by_user
    self.split_type: ExpenseSplitType = split_type
    self.split_details: List[Split] = list(split_details)