from typing import Dict
from balance import Balance

class UserExpenseBalanceSheet:
  def __init__(self):
    self.user_vs_balance: Dict[str, Balance] = {}
    self.total_your_expense: float = 0
    self.total_payment: float = 0
    self.total_you_owe: float = 0
    self.total_you_get_back: float = 0
  
  def getUserVsBalance(self) -> Dict[str, Balance]:
    return self.user_vs_balance
  
  def getTotalYourExpense(self) -> float:
    return self.total_your_expense
  
  def setTotalYourExpense(self, total_your_expense: float):
    self.total_your_expense = total_your_expense

  def getTotalYouOwe(self) -> float:
    return self.total_you_owe
  
  def setTotalYouOwe(self, total_you_owe: float):
    self.total_you_owe = total_you_owe

  def getTotalYouGetBack(self) -> float:
    return self.total_you_get_back
  
  def setTotalYouGetBack(self, total_you_get_back: float):
    self.total_you_get_back = total_you_get_back

  def getTotalPayment(self) -> float:
    return self.total_payment
  
  def setTotalPayment(self, total_payment: float):
    self.total_payment = total_payment