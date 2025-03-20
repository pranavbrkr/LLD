from city import City
from movie_factory import MovieFactory
from screen import Screen
from seat import Seat
from show import Show
from theatre_factory import TheatreFactory

class BookingDataFactory:
  @staticmethod
  def createSeats():
    seats = []
    for i in range(1, 101):
      seat = Seat()
      seat.setSeatId(i)
      seats.append(seat)
    return seats

  @staticmethod
  def createScreens():
    screens = []
    screen1 = Screen()
    screen1.setScreenId(1)
    screen1.setSeats(BookingDataFactory.createSeats())
    screens.append(screen1)
    return screens
  
  @staticmethod
  def createShow(show_id, movie, show_start_time):
    show = Show()
    show.setShowId(show_id)
    show.setMovie(movie)
    show.setShowStartTime(show_start_time)
    return show
  
  @staticmethod
  def createMovies(movie_controller):
    barbie = MovieFactory.createMovie(1, "BARBIE", 128)
    oppenheimer = MovieFactory.createMovie(2, "OPPENHEIMER", 180)

    movie_controller.addMovie(barbie, City.Bangalore)
    movie_controller.addMovie(barbie, City.Delhi)
    movie_controller.addMovie(oppenheimer, City.Bangalore)
    movie_controller.addMovie(oppenheimer, City.Delhi)

    return [barbie, oppenheimer]
  
  @staticmethod
  def createTheatres(movie_controller, theatre_controller):
    barbie = movie_controller.getMovieByName("BARBIE")
    oppenheimer = movie_controller.getMovieByName("OPPENHEIMER")

    inox = TheatreFactory.createTheatre(
        1, "INOX", City.Bangalore,
        [
            BookingDataFactory.createShow(1, barbie, 10),
            BookingDataFactory.createShow(2, oppenheimer, 18)
        ]
    )
    pvr = TheatreFactory.createTheatre(
        2, "PVR", City.Delhi,
        [
            BookingDataFactory.createShow(3, barbie, 14),
            BookingDataFactory.createShow(4, oppenheimer, 20)
        ]
    )

    theatre_controller.addTheatre(inox, City.Bangalore)
    theatre_controller.addTheatre(pvr, City.Delhi)