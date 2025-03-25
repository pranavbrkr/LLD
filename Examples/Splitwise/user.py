from user_expense_balance_sheet import UserExpenseBalanceSheet

class User:
  def __init__(self, user_id: str, user_name: str):
    self.user_id: str = user_id
    self.user_name: str = user_name
    self.user_expense_balance_sheet: UserExpenseBalanceSheet = UserExpenseBalanceSheet()

  def getUserId(self) -> str:
    return self.user_id
  
  def getUserExpenseBalanceSheet(self) -> UserExpenseBalanceSheet:
    return self.user_expense_balance_sheet

  def getUserName(self) -> str:
    return self.user_name