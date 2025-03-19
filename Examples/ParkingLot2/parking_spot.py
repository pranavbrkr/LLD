from abc import ABC, abstractmethod

from vehicle import Vehicle

class ParkingSpot(ABC):
  def __init__(self, spot_number: int, spot_type: str):
    self.spot_number = spot_number
    self.is_occupied = False
    self.spot_type = spot_type
    self.vehicle = None

  @abstractmethod
  def canParkVehicle(self, vehicle: Vehicle) -> bool:
    pass

  def parkVehicle(self, vehicle: Vehicle) -> None:
    if self.is_occupied:
      raise RuntimeError("Spot is already occupied")
    if not self.canParkVehicle(vehicle):
      raise ValueError(f"This spot is not suitable for {vehicle.vehicle_type}")
    self.vehicle = vehicle
    self.is_occupied = True
  
  def vacate(self):
    if not self.is_occupied:
      raise RuntimeError("Spot is already vacant")
    self.vehicle = None
    self.is_occupied = False
  
  def getSpotNumber(self) -> int:
    return self.spot_number
  
  def getVehicle(self) -> Vehicle:
    return self.vehicle
  
  def __str__(self) -> str:
    vehicle_plate = self.vehicle.license_plate if self.vehicle is not None else "None"
    return (f"Parking spot{{spotNumber={self.spot_number}, isOccupied={self.is_occupied}, vehicle={vehicle_plate}}}")
  
  def getSpotType(self) -> str:
    return self.spot_type