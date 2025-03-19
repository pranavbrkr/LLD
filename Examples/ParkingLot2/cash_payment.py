from payment_strategy import PaymentStrategy

class CashPayment(PaymentStrategy):
  def processPayment(self, amount: float) -> None:
    return f"Processing cash payment of ${amount}"