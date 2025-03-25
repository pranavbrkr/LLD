class Balance:
  def __init__(self, amount_owe: float = 0, amount_get_back: float = 0):
    self.amount_owe = amount_owe
    self.amount_get_back = amount_get_back

  def getAmountOwe(self) -> float:
    return self.amount_owe
  
  def setAmountOwe(self, amount_owe: float):
    self.amount_owe = amount_owe

  def getAmountGetBack(self) -> float:
    return self.amount_get_back
  
  def setAmountGetBack(self, amount_get_back: float):
    self.amount_get_back = amount_get_back
  
