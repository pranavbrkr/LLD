from payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
  def processPayment(self, amount: float) -> None:
    return f"Processing credit card payment of ${amount}"