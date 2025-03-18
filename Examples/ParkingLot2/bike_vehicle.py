from vehicle import Vehicle


class BikeVehicle(Vehicle):
  RATE = 5

  def __init__(self, license_plate: str):
    super().__init__(license_plate, "Bike")

  def calculateFee(self, hours_stayed: int) -> float:
    return hours_stayed * self.RATE