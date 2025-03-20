from typing import List
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot
from vehicle import Vehicle


class ParkingLot:
  def __init__(self, floors: List[ParkingFloor]):
    self.floors = floors
  
  def findAvailableSpot(self, vehicle_type: str) -> ParkingSpot:
    for floor in self.floors:
      spot = floor.findAvailableSpot(vehicle_type)
      if spot is not None:
        return spot
    return None
  
  def parkVehicle(self, vehicle: Vehicle) -> ParkingSpot:
    spot = self.findAvailableSpot(vehicle.vehicle_type)
    if spot is not None:
      spot.parkVehicle(vehicle)
      print(f"Vehicle parked successfully in spot: ", spot.getSpotNumber())
      return spot
    print(f"No parking spots available for {vehicle.vehicle_type}!")
    return None

  def vacateSpot(self, spot: ParkingSpot, vehicle: Vehicle):
    if spot is not None and spot.is_occupied and spot.getVehicle() == vehicle:
      spot.vacate()
      print(f"{vehicle.vehicle_type} vacated the spot: {spot.getSpotNumber()}")
    else:
      print("Invalid operation! Either spot is already vacant or vehicle does not match")
  
  def getSpotByNumber(self, spot_number: int) -> ParkingSpot:
    for floor in self.floors:
      for spot in floor.getParkingSpots():
        if spot.getSpotNumber() == spot_number:
          return spot
    return None
  
  def getFloors(self) -> ParkingFloor:
    return self.floors