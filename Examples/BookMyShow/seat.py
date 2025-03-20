class Seat:
  def __init__(self, seat_id = None, row = None, seat_category = None):
    self._seat_id = seat_id
    self._row = row
    self._seat_category = seat_category

  def getSeatId(self):
    return self._seat_id
  
  def setSeatId(self, seat_id):
    self._seat_id = seat_id

  def getRow(self):
    return self._row
  
  def setRow(self, row):
    self._row = row

  def getSeatCategory(self):
    return self._seat_category
  
  def setSeatCategory(self, seat_category):
    self._seat_category = seat_category