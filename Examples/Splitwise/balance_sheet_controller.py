from typing import List
from user import User
from split import Split
from balance import Balance
from user_expense_balance_sheet import UserExpenseBalanceSheet

class BalanceSheetController:
  def updateUserExpenseBalanceSheet(self, payer: User, splits: List[Split], total_expense: float):
    payer_sheet: UserExpenseBalanceSheet = payer.getUserExpenseBalanceSheet()
    payer_sheet.setTotalPayment(payer_sheet.getTotalPayment() + total_expense)

    for split in splits:
      person_who_owes: User = split.getUser()
      owes_sheet: UserExpenseBalanceSheet = person_who_owes.getUserExpenseBalanceSheet()
      amount_to_pay: float = split.getAmountOwe()

      if payer.getUserId() == person_who_owes.getUserId():
        payer_sheet.setTotalYourExpense(payer_sheet.getTotalYourExpense() + amount_to_pay)
      else:
        payer_sheet.setTotalYouGetBack(payer_sheet.getTotalYouGetBack() + amount_to_pay)
        
        payer_balance: Balance = payer_sheet.getUserVsBalance().setdefault(person_who_owes.getUserId(), Balance())
        payer_balance.setAmountGetBack(payer_balance.getAmountGetBack() + amount_to_pay)

        owes_sheet.setTotalYouOwe(owes_sheet.getTotalYouOwe() + amount_to_pay)
        owes_sheet.setTotalYourExpense(owes_sheet.getTotalYourExpense() + amount_to_pay)

        owes_balance: Balance = owes_sheet.getUserVsBalance().setdefault(payer.getUserId(), Balance())
        owes_balance.setAmountOwe(owes_balance.getAmountOwe() + amount_to_pay)
    
  def showBalanceSheetOfUser(self, user: User):
    print("--------------------------")
    print(f"Balance sheet of user {user.getUserId()}")

    user_expense_balance_sheet: UserExpenseBalanceSheet = user.getUserExpenseBalanceSheet()

    print(f"TotalYourExpense: {user_expense_balance_sheet.getTotalYourExpense()}")
    print(f"TotalGetBack: {user_expense_balance_sheet.getTotalYouGetBack()}")
    print(f"TotalYouOwe: {user_expense_balance_sheet.getTotalYouOwe()}")
    print(f"TotalPaymentMade: {user_expense_balance_sheet.getTotalPayment()}")

    for user_id, balance in user_expense_balance_sheet.getUserVsBalance().items():
      print(f"userID: {user_id}, YouGetBack: {balance.getAmountGetBack()}, YouOwe: {balance.getAmountOwe()}")
    
    print("--------------------------")