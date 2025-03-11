from typing import List
from level import Level
from vehicle import Vehicle

class ParkingLot:
  _instance = None

  def __init__(self):
    if ParkingLot._instance is not None:
      raise Exception('This class is a singleton!')
    else:
      ParkingLot._instance = self
      self.levels: List[Level] = []
    
    @staticmethod
    def getInstance():
      if ParkingLot._instance is None:
        ParkingLot()
      return ParkingLot._instance
    
    def parkVehicle(self, vehicle: Vehicle) -> bool:
      for level in self.levels:
        if level.parkVehicle(vehicle):
          return True
      return False
    
    def unparkVehicle(self, vehicle: Vehicle) -> bool:
      for level in self.levels:
        if level.unparkVehicle(vehicle):
          return True
      return False
    
    def displayAvailabilty(self) -> None:
      for level in self.levels:
        level.displayAvailability()