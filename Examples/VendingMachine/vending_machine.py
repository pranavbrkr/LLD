from threading import Lock
from inventory import Inventory
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from return_change_state import ReturnChangeState
from vending_machine_state import VendingMachineState
from product import Product
from coin import Coin
from note import Note

class VendingMachine:
  _instance = None
  _lock = Lock()

  def __new__(cls):
    with cls._lock:
      if cls._instance is None:
        cls._instance = super().__new__(cls)
        cls._instance.inventory = Inventory()
        cls._instance.idle_state = IdleState(cls._instance)
        cls._instance.ready_state = ReadyState(cls._instance)
        cls._instance.dispense_state = DispenseState(cls._instance)
        cls._instance.return_change_state = ReturnChangeState(cls._instance)
        cls._instance.current_state = cls._instance.idle_state
        cls._instance.selected_product = None
        cls._instance.total_payment = 0
    return cls._instance
  
  @classmethod
  def getInstance(cls):
    return cls()
  
  def selectProduct(self, product: Product):
    self.current_state.selectProduct(product)
  
  def insertCoin(self, coin: Coin):
    self.current_state.insertCoin(coin)
  
  def insertNote(self, note: Note):
    self.current_state.insertNote(note)
  
  def dispenseProduct(self):
    self.current_state.dispenseProduct()
  
  def returnChange(self):
    self.current_state.returnChange()
  
  def setState(self, state: VendingMachineState):
    self.current_state = state
  
  def addCoin(self, coin: Coin):
    self.total_payment += coin.value
  
  def addNote(self, note: Note):
    self.total_payment += note.value
  
  def resetPayment(self):
    self.total_payment = 0
  
  def resetSelectedProduct(self):
    self.selected_product = None