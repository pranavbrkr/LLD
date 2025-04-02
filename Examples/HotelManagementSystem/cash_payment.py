from payment import Payment

class CashPayment(Payment):
  def processPayment(self, amount: float):
    print(f"Cash payment of ${amount} done")
    return True