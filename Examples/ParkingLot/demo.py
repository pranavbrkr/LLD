from vehicle_type import VehicleType
from parking_lot import ParkingLot
from level import Level
from car import Car
from motorcycle import Motorcycle
from truck import Truck
from vehicle_factory import VehicleFactory

if __name__ == "__main__":
  parking_lot = ParkingLot.getInstance()
  parking_lot.addLevel(Level(1, 100))
  parking_lot.addLevel(Level(2, 80))

  car = VehicleFactory.createVehicle(VehicleType.CAR, "ABC123")
  motorcycle = VehicleFactory.createVehicle(VehicleType.MOTORCYCLE, "XYZ456")
  truck = VehicleFactory.createVehicle(VehicleType.TRUCK, "LMN789")

  parking_lot.parkVehicle(car)
  parking_lot.parkVehicle(motorcycle)
  parking_lot.parkVehicle(truck)

  parking_lot.displayAvailability()

  parking_lot.unparkVehicle(motorcycle)

  parking_lot.displayAvailability()