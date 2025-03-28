from abc import ABC, abstractmethod
from coin import Coin
from note import Note
from product import Product

class VendingMachineState(ABC):
  def __init__(self, vending_machine):
    self.vending_machine = vending_machine
  
  @abstractmethod
  def selectProduct(self, product: Product):
    pass

  @abstractmethod
  def insertCoin(self, coin: Coin):
    pass

  @abstractmethod
  def insertNote(self, note: Note):
    pass

  @abstractmethod
  def dispenseProduct(self):
    pass

  @abstractmethod
  def returnChange(self):
    pass