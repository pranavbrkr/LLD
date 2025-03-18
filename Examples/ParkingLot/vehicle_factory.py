from vehicle_type import VehicleType
from car import Car
from truck import Truck
from motorcycle import Motorcycle

class VehicleFactory:
    @staticmethod
    def createVehicle(vehicle_type: VehicleType, license_plate: str):
        if vehicle_type == VehicleType.CAR:
            return Car(license_plate)
        elif vehicle_type == VehicleType.TRUCK:
            return Truck(license_plate)
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle(license_plate)
        else:
            raise ValueError("Unsupported vehicle type")