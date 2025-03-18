from car_vehicle import CarVehicle
from bike_vehicle import BikeVehicle


class VehicleFactory:
  @staticmethod
  def createVehicle(vehicle_type: str, license_plate: str):
    if vehicle_type.lower() == "car":
      return CarVehicle(license_plate)
    elif vehicle_type.lower() == "bike":
      return BikeVehicle(license_plate)