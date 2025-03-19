from cash_payment import CashPayment
from credit_card_payment import CreditCardPayment
from payment import Payment


class PaymentService:
  def __init__(self):
    pass

  def processPayment(self, fee: float) -> None:
    self.choosePaymentMethod(fee)
  
  def choosePaymentMethod(self, fee: float) -> None:
    print(f"Total fee: ${fee}")
    print("Choose payment method")
    print("1. Credit card")
    print("1. Cash")

    try:
      choice = int(input("Enter your choice: "))
    except ValueError:
      print("Invalid input! Defaulting to cash payment")
      choice = 2
    
    if choice == 1:
      payment = Payment(fee,  CreditCardPayment())
    elif choice == 2:
      payment = Payment(fee, CashPayment())
    else:
      print("Invalid input! Defaulting to cash payment")
      payment = Payment(fee, CashPayment())
    
    payment.processPayment()