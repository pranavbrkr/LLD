import threading
from typing import List, Optional
from balance_sheet_controller import BalanceSheetController
from group_controller import GroupController
from user_controller import UserController
from group import Group
from user import User
from expense_split_type import ExpenseSplitType
from split import Split

class Splitwise:
  _instance: Optional["Splitwise"] = None
  _lock = threading.Lock()

  def __init__(self):
    self.user_controller: UserController = UserController()
    self.group_controller: GroupController = GroupController()
    self.balance_sheet_controller: BalanceSheetController = BalanceSheetController()

  @classmethod
  def getInstance(cls) -> "Splitwise":
    if cls._instance is None:
      with cls._lock:
        if cls._instance is None:
          cls._instance = cls()
    return cls._instance
  
  def registerUsers(self):
    self.user_controller.addUser(User("U1001", "Alice"))
    self.user_controller.addUser(User("U2001", "Bob"))
    self.user_controller.addUser(User("U3001", "Charlie"))
  
  def setupUsersAndGroup(self):
    self.registerUsers()
    self.group_controller.createNewGroup("G1001", "Outing with friends", self.user_controller.getUser("U1001"))
  
  def runSplitwiseDemo(self):
    self.setupUsersAndGroup()

    group: Optional[Group] = self.group_controller.getGroup("G1001")
    
    if group is not None:
      group.addMember(self.user_controller.getUser("U2001"))
      group.addMember(self.user_controller.getUser("U3001"))

      group.createExpense(
        "Exp1001",
        "Breakfast",
        900,
        [
          Split(self.user_controller.getUser("U1001"), 300),
          Split(self.user_controller.getUser("U2001"), 300),
          Split(self.user_controller.getUser("U3001"), 300),
        ],
        ExpenseSplitType.EQUAL,
        self.user_controller.getUser("U1001")
      )

      group.createExpense(
        "Exp1002",
        "Lunch",
        500,
        [
          Split(self.user_controller.getUser("U1001"), 400),
          Split(self.user_controller.getUser("U2001"), 100),
        ],
        ExpenseSplitType.UNEQUAL,
        self.user_controller.getUser("U2001")
      )
    
    for user in self.user_controller.getAllUsers():
      self.balance_sheet_controller.showBalanceSheetOfUser(user)