from typing import List
from parking_spot import ParkingSpot
from bike_parking_spot import BikeParkingSpot
from car_parking_spot import CarParkingSpot


class ParkingFloor:
  def __init__(self, floor_number: int, num_of_car_spots: int, num_of_bike_spots: int):
    self.floor_number = floor_number
    self.spots: List[ParkingSpot] = []

    for i in range(num_of_car_spots):
      self.spots.append(CarParkingSpot(i + 1))

    for i in range(num_of_car_spots, num_of_car_spots + num_of_bike_spots):
      self.spots.append(BikeParkingSpot(i + 1))
  
  def findAvailableSpot(self, vehicle_type: str):
    for spot in self.spots:
      if not spot.is_occupied and spot.getSpotType().lower() == vehicle_type.lower():
        return spot
    return None
  
  def getParkingSpots(self):
    return self.spots