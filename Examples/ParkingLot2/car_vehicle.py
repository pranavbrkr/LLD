from vehicle import Vehicle


class CarVehicle(Vehicle):
  RATE = 10

  def __init__(self, license_plate: str):
    super().__init__(license_plate, "Car")

  def calculateFee(self, hours_stayed: int) -> float:
    return hours_stayed * self.RATE