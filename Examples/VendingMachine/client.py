from vending_machine import VendingMachine
from product import Product
from coin import Coin
from note import Note

class Client:
  @staticmethod
  def run():
    vending_machine = VendingMachine.getInstance()

    coke = Product("Coke", 1.5)
    pepsi = Product("Pepsi", 1.5)
    water = Product("Water", 1.0)

    vending_machine.inventory.addProduct(coke, 5)
    vending_machine.inventory.addProduct(pepsi, 3)
    vending_machine.inventory.addProduct(water, 2)

    vending_machine.selectProduct(coke)

    vending_machine.insertCoin(Coin.QUARTER)
    vending_machine.insertCoin(Coin.QUARTER)
    vending_machine.insertCoin(Coin.QUARTER)
    vending_machine.insertCoin(Coin.QUARTER)

    vending_machine.insertNote(Note.FIVE)

    vending_machine.dispenseProduct()

    vending_machine.returnChange()

    vending_machine.selectProduct(pepsi)

    vending_machine.insertCoin(Coin.QUARTER)

    vending_machine.dispenseProduct()

    vending_machine.insertCoin(Coin.QUARTER)
    vending_machine.insertCoin(Coin.QUARTER)
    vending_machine.insertCoin(Coin.QUARTER)
    vending_machine.insertCoin(Coin.QUARTER)

    vending_machine.dispenseProduct()

    vending_machine.returnChange()

if __name__ == "__main__":
  Client.run()