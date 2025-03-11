from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
  def __init__(self, spot_number: int):
    self.spot_number = spot_number
    self.vehicle_type = VehicleType.CAR
    self.parked_vehicle = None

  def isAvailable(self) -> bool:
    return self.parked_vehicle is None
  
  def parkVehicle(self, vehicle: Vehicle) -> None:
    if self.isAvailable() and vehicle.getType() == self.vehicle_type:
      self.parked_vehicle = vehicle
    else:
      raise ValueError("Invalid vehicle type or spot already occupied")
  
  def unparkVehicle(self) -> None:
    self.parked_vehicle = None
  
  def getVehicleType(self) -> VehicleType:
    return self.vehicle_type
  
  def getParkedVehicle(self) -> Vehicle:
    return self.parked_vehicle

  def getSpotNumber(self) -> int:
    return self.spot_number