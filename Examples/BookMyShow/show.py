class Show:
  def __init__(self, show_id = None, movie = None, screen = None, show_start_time = None, booked_seat_ids = None):
    self._show_id = show_id
    self._movie = movie
    self._screen = screen
    self._show_start_time = show_start_time
    self._booked_seat_ids = booked_seat_ids if booked_seat_ids is not None else []
  
  def getShowId(self):
    return self._show_id
  
  def setShowId(self, show_id):
    self._show_id = show_id
  
  def getMovie(self):
    return self._movie
  
  def setMovie(self, movie):
    self._movie = movie
  
  def getScreen(self):
    return self._screen
  
  def setScreen(self, screen):
    self._screen = screen
  
  def getShowStartTime(self):
    return self._show_start_time
  
  def setShowStartTime(self, show_start_time):
    self._show_start_time = show_start_time
  
  def getBookedSeatIds(self):
    return self._booked_seat_ids
  
  def setBookedSeatIds(self, booked_seat_ids):
    self._booked_seat_ids = booked_seat_ids