from user import User

class Split:
  def __init__(self, user: User, amount_owe: float):
    self.user = user
    self.amount_owe = amount_owe

  def getUser(self) -> User:
    return self.user
  
  def setUser(self, user: User):
    self.user = user
  
  def getAmountOwe(self) -> float:
    return self.amount_owe
  
  def setAmountOwe(self, amount_owe: float):
    self.amount_owe = amount_owe