from payment_strategy import PaymentStrategy

class Payment:
  def __init__(self, amount: float, payment_strategy: PaymentStrategy):
    self.amount = amount
    self.payment_strategy = payment_strategy
  
  def processPayment(self):
    if self.amount > 0:
      self.payment_strategy.processPayment(self.amount)
    else:
      print("Invalid payment amount")