from typing import List
from vehicle import Vehicle
from parking_spot import ParkingSpot


class Level:
  def __init__(self, floor: int, num_spots: int):
    self.floor = floor
    self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(num_spots)]

  def parkVehicle(self, vehicle: Vehicle) -> bool:
    for spot in self.parking_spots:
      if spot.isAvailable() and spot.getVehicleType() == vehicle.getType():
        spot.parkVehicle(vehicle)
        return True
    return False
  
  def unparkVehicle(self, vehicle: Vehicle) -> bool:
    for spot in self.parking_spots:
      if not spot.isAvailable() and spot.getParkedVehicle() == vehicle:
        spot.unparkVehicle()
        return True
    return False
  
  def displayAvailability(self) -> None:
    print(f"Level {self.floor} availability:")
    for spot in self.parking_spots:
      print(f"Spot {spot.getSpotNumber()}: {'Available' if spot.isAvailable() else 'Occupied'}")