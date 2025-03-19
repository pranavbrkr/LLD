from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
  @abstractmethod
  def processPayment(self, amount: float) -> None:
    pass