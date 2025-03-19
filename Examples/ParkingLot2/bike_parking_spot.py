from parking_spot import ParkingSpot
from vehicle import Vehicle

class BikeParkingSpot(ParkingSpot):
  def __init__(self, spot_number: int):
    super().__init__(spot_number, "Bike")

  def canParkVehicle(self, vehicle: Vehicle):
    return vehicle.vehicle_type.lower() == "bike"