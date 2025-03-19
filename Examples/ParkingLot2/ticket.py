from datetime import datetime
from vehicle import Vehicle
from parking_spot import ParkingSpot

class Ticket:
  def __init__(self, parking_spot: ParkingSpot, vehicle: Vehicle):
    self.parking_spot = parking_spot
    self.vehicle = vehicle
    self.start_time = datetime.now()