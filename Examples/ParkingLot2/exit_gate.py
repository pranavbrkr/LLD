from Examples.ParkingLot2.parking_lot import ParkingLot
from Examples.ParkingLot2.payment_service import PaymentService


class ExitGate:
  def __init__(self, parking_lot: ParkingLot, payment_service: PaymentService):
    self.parking_lot = parking_lot
    self.payment_service = payment_service

  def processExit(self, spot_number: int, hours_stayed: int):
    spot = self.parking_lot.getSpotByNumber(spot_number)

    if spot is None or not spot.is_occupied:
      print("Invalid or vacant spot")
      return

    vehicle = spot.getVehicle()
    if vehicle is None:
      print("No vehicle found in the spot!")
      return
    
    fee = vehicle.calculateFee(hours_stayed)
    self.payment_service.processPayment(fee)
    self.parking_lot.vacateSpot(spot, vehicle)
    print("Spot vacated successfully!")