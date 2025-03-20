import uuid
import datetime
from booking_data_factory import BookingDataFactory
from city import City
from payment_service import PaymentService
from movie_controller import MovieController
from theatre_controller import TheatreController

class BookingService:
  _instance = None

  def __init__(self):
    self.movie_controller = MovieController()
    self.theatre_controller = TheatreController()
  
  @classmethod
  def getInstance(cls):
    if cls._instance is None:
      cls._instance = BookingService()
    return cls._instance

  def startBookingSession(self):
    self.printHeader("Welcome to BookMyShow")
    continue_booking = True

    while continue_booking:
      user_city = self.selectCity()
      selected_movie = self.selectMovie(user_city)
      selected_show = self.selectShow(user_city, selected_movie)
      self.bookSeat(selected_show)

      response = input("Do you want to book another ticket (yes/no): ").strip().lower()
      continue_booking = (response == "yes")
    
    self.printSuccess("Thank you for using BookMyShow! Have a great day!")
  
  def selectCity(self):
    self.printSection("Select your city")
    cities = list(City)
    for idx, city in enumerate(cities, start = 1):
      print(f"   {idx}. {city.value}")
    choice = self.getUserChoice(1, len(cities))
    return cities[choice - 1]

  def selectMovie(self, city):
    movies = self.movie_controller.getMoviesByCity(city)
    self.printSection(f"Available movies in {city.value}")
    for idx, movie in enumerate(movies ,start = 1):
      print(f"   {idx}. {movie.getMovieName()}")
    choice = self.getUserChoice(1, len(movies))
    return movies[choice - 1]

  def selectShow(self, city, movie):
    shows_map = self.theatre_controller.getAllShow(movie, city)
    available_shows = []
    self.printSection(f"Avaiable shows for {movie.getMovieName()} in {city.value}")
    index = 1
    for theatre, shows in shows_map.items():
      for show in shows:
        print(f"   {index}. {show.getShowStartTime()} at {theatre.getTheatreName()}")
        available_shows.append(show)
        index += 1
    
    choice = self.getUserChoice(1, len(available_shows))
    return available_shows[choice - 1]

  def bookSeat(self, show):
    self.printSection("Select your Seat (1-100)")
    seat_number = self.getUserChoice(1, 100)
    if seat_number in show.getBookedSeatIds():
      print("Seat already booked! Please try another seat")
      self.bookSeat(show)
    else:
      show.getBookedSeatIds().append(seat_number)
      payment_service = PaymentService()
      payment_success = payment_service.processPayment(250)

      if payment_success:
        self.printSuccess("Booking successful! Enjoy your movie!")
        self.generateTicket(show, seat_number)
      else:
        print("Payment failed! Please try again!")
        show.getBookedSeatIds().remove(seat_number)

  def getUserChoice(self, min_val, max_val):
    while True:
      try:
        choice = int(input(f"Enter choice ({min_val}-{max_val}): "))
        if min_val <= choice <= max_val:
          return choice
        else:
          print(f"Invalid choice! Please enter a number between {min_val} and {max_val}.")
      except ValueError:
        print("Invalid input! Please enter a number.")

  def generateTicket(self, show, seat_number):
    print("\n========================================")
    print("       MOVIE TICKET CONFIRMATION       ")
    print("========================================")
    print("Movie: " + show.getMovie().getMovieName())
    print("Show Time: " + str(show.getShowStartTime()) + ":00")
    print("Seat Number: " + str(seat_number))
    print("----------------------------------------")
    print("Date: " + str(datetime.date.today()))
    print("Booking ID: " + str(uuid.uuid4()))
    print("========================================")
    print("Enjoy your movie! Have a great time!")
    print("========================================\n")

  def printHeader(self, text):
    print("\n══════════════════════════════════════════")
    print("          " + text)
    print("══════════════════════════════════════════\n")

  def printSection(self, text):
    print("\n " + text)
    print("──────────────────────────────────────────")

  def printSuccess(self, text):
    print("\n " + text + "\n")
  
  def initialize(self):
    BookingDataFactory.createMovies(self.movie_controller)
    BookingDataFactory.createTheatres(self.movie_controller, self.theatre_controller)