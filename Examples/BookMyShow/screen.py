class Screen:
  def __init__(self, screen_id = None, seats = None):
    self._screen_id = screen_id
    self._seats = seats if seats is not None else []

  def getScreenId(self):
    return self._screen_id

  def setScreenId(self, screen_id):
    self._screen_id = screen_id

  def getSeats(self):
    return self._seats

  def setSeats(self, seats):
    self._seats = seats