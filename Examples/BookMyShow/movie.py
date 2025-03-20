class Movie:
  def __init__(self, movie_id: int, movie_name: str, movie_duration_in_minutes: int):
    self._movie_id = movie_id
    self._movie_name = movie_name
    self._movie_duration_in_minutes = movie_duration_in_minutes

  def getMovieId(self) -> int:
    return self._movie_id
  
  def setMovieId(self, movie_id: int):
    self._movie_id = movie_id

  def getMovieName(self) -> str:
    return self._movie_name
  
  def setMovieName(self, movie_name: str):
    self._movie_name = movie_name

  def getMovieDuration(self) -> int:
    return self._movie_duration_in_minutes
  
  def setMovieId(self, movie_duration: int):
    self._movie_duration_in_minutes = movie_duration