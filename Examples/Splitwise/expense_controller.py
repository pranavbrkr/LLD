from typing import List
from expense import Expense
from expense_split_type import ExpenseSplitType
from split import Split
from expense_split_strategy import ExpenseSplitStrategy
from equal_expense_split import EqualExpenseSplit
from unequal_expense_split import UnequalExpenseSplit
from percentage_expense_split import PercentageExpenseSplit
from user import User
from balance_sheet_controller import BalanceSheetController

class ExpenseController:
  def __init__(self):
    self.balance_sheet_controller: BalanceSheetController = BalanceSheetController()

  def createExpense(self, expense_id: str, description: str, expense_amount: float, split_details: List[Split], split_type: ExpenseSplitType, paid_by_user: User) -> Expense:
    if split_type == ExpenseSplitType.EQUAL:
      expense_split: ExpenseSplitStrategy = EqualExpenseSplit()
    elif split_type == ExpenseSplitType.UNEQUAL:
      expense_split: ExpenseSplitStrategy = UnequalExpenseSplit()
    elif split_type == ExpenseSplitType.PERCENTAGE:
      expense_split: ExpenseSplitStrategy = PercentageExpenseSplit()
    else:
      raise ValueError("Invalid split type")
    
    expense_split.validateSplitRequest(split_details, expense_amount)
    expense = Expense(expense_id, expense_amount, description, paid_by_user, split_type, split_details)
    self.balance_sheet_controller.updateUserExpenseBalanceSheet(paid_by_user, split_details, expense_amount)

    return expense