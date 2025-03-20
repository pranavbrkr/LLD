class TheatreController:
  def __init__(self):
    self.city_vs_theatre = {}
    self.all_theatre = []

  def addTheatre(self, theatre, city):
    self.all_theatre.append(theatre)
    theatres = self.city_vs_theatre.get(city, [])
    theatres.append(theatre)
    self.city_vs_theatre[city] = theatres
  
  def getAllShow(self, movie, city):
    theatre_vs_shows = {}
    theatres = self.city_vs_theatre.get(city, [])
    for theatre in theatres:
      given_movie_shows = []
      shows = theatre.getShows()
      for show in shows:
        if show.getMovie().getMovieId() == movie.getMovieId():
          given_movie_shows.append(show)
      if given_movie_shows:
        theatre_vs_shows[theatre] = given_movie_shows
    return theatre_vs_shows