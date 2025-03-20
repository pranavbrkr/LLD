from parking_lot import ParkingLot
from vehicle_factory import VehicleFactory


class EntranceGate:
  def __init__(self, parking_lot: ParkingLot):
    self.parking_lot = parking_lot
  
  def processEntrance(self):
    license_plate = input("Enter the vehicle license plate: ")
    vehicle_type = input("Enter the vehicle type (Car or Bike): ")

    vehicle = VehicleFactory.createVehicle(vehicle_type, license_plate)
    if vehicle is None:
      print("Invalid vehicle type! Only Car and Bike are allowed")
      return
    
    spot = self.parking_lot.parkVehicle(vehicle)
    if spot is not None:
      print(f"Vehicle parked successfully in spot: {spot.getSpotNumber()}")
    else:
      print("No available spots for the vehicle type")