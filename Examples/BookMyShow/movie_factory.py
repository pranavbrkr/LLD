from movie import Movie


class MovieFactory:
  movie_cache = {}
  
  @classmethod
  def createMovie(cls, movie_id, name, duration):
    if name not in cls.movie_cache:
      cls.movie_cache[name] = Movie(movie_id, name, duration)
    return cls.movie_cache[name]