from seat import Seat
from screen import Screen
from theatre import Theatre


class TheatreFactory:
  @staticmethod
  def createTheatre(theatre_id, name, city, shows):
    theatre = Theatre()
    theatre.setTheatreId(theatre_id)
    theatre.setTheatreName(name)
    theatre.setScreen(TheatreFactory.createScreens())
    theatre.setCity(city)
    theatre.setShows(shows)
    return theatre
  
  @staticmethod
  def createScreens():
    screen = Screen()
    screen.setScreenId(1)
    screen.setSeats(TheatreFactory.createSeats())
    return [screen]
  
  @staticmethod
  def createSeats():
    seats = []
    for i in range(1, 101):
      seats.append(Seat())
    return seats