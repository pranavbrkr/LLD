from entrance_gate import EntranceGate
from exit_gate import ExitGate
from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from payment_service import PaymentService


def showMenu():
  print("\n*************************")
  print("Please choose an option from below:")
  print("1. Park a vehicle")
  print("2. Vacate a vehicle spot")
  print("3. Exit the system")
  print("*************************")

def getUserChoice():
  return int(input("Enter your choice: "))

def parkVehicle(entrance_gate: EntranceGate):
  entrance_gate.processEntrance()

def vacateSpot(exit_gate: ExitGate):
  spot_number = int(input("Enter the spot number to vacate: "))
  hours_stayed = int(input("Enter the number of hours the vehicle stayed: "))
  exit_gate.processExit(spot_number, hours_stayed)

if __name__ == "__main__":
  floor = ParkingFloor(1, 2, 2)
  floors = [floor]
  parking_lot = ParkingLot(floors)

  payment_service = PaymentService()
  
  entrance_gate = EntranceGate(parking_lot)
  exit_gate = ExitGate(parking_lot, payment_service)

  print("\n================================")
  print("Welcome to the parking lot system!")
  print("================================")

  exit_flag = False
  while not exit_flag:
    showMenu()
    try:
      choice = getUserChoice()
    except ValueError:
      print("Invalid input! Please enter a valid number")
      continue

    if choice == 1:
      parkVehicle(entrance_gate)
    elif choice == 2:
      vacateSpot(exit_gate)
    elif choice == 3:
      exit_flag = True
      print("Thank you for using Parking Lot System!")
    else:
      print("Invalid option! Please try again")