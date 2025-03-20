class MovieController:
  def __init__(self):
    self.city_vs_movies = {}
    self.all_movies = []

  def addMovie(self, movie, city):
    self.all_movies.append(movie)
    movies = self.city_vs_movies.get(city, [])
    movies.append(movie)
    self.city_vs_movies[city] = movies
  
  def getMovieByName(self, movie_name):
    for movie in self.all_movies:
      if movie.getMovieName() == movie_name:
        return movie
    return None
  
  def getMoviesByCity(self, city):
    return self.city_vs_movies.get(city, [])