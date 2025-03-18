from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, license_plate: str, vehicle_type: str):
    self.license_plate = license_plate
    self.vehicle_type = vehicle_type

  def getLicensePlate(self) -> str:
    return self.license_plate

  def getVehicleType(self) -> str:
    return self.vehicle_type
  
  @abstractmethod
  def calculateFee(self, hours_stayed: int) -> float:
    pass