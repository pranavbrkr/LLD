class Theatre:
  def __init__(self, theatre_id = None, address = None, theatre_name = None, city = None, screen = None, shows = None):
    self._theatre_id = theatre_id
    self._address = address
    self._theatre_name = theatre_name
    self._city = city
    self._screen = screen if screen is not None else []
    self._shows = shows if shows is not None else []
  
  def getTheatreId(self):
    return self._theatre_id
  
  def setTheatreId(self, theatre_id):
    self._theatre_id = theatre_id
  
  def getAddress(self):
    return self._address
  
  def setAddress(self, address):
    self._address = address
  
  def getTheatreName(self):
    return self._theatre_name
  
  def setTheatreName(self, theatre_name):
    self._theatre_name = theatre_name
  
  def getCity(self):
    return self._city
  
  def setCity(self, city):
    self._city = city
  
  def getScreen(self):
    return self._screen
  
  def setScreen(self, screen):
    self._screen = screen
  
  def getShows(self):
    return self._shows
  
  def setShows(self, shows):
    self._shows = shows