from payment import Payment

class CreditCardPayment(Payment):
  def processPayment(self, amount: float):
    print(f"Credit card payment of ${amount} done")
    return True