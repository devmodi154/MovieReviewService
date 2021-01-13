from models.Movie import Movie
from models.Role import Viewer
import datetime

class User():
    def __init__(self, name:str) -> None:
        self._name = name
        self._rated_movies = set() 
        self.role = Viewer()

    # Setter Getters
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str) -> None:
        self._name = value

    @property
    def rated_movies(self) -> set:
        return self._rated_movies
    @rated_movies.setter
    def rated_movies(self, value:set) -> None:
        self._rated_movies = value
    # Setter Getters End


    def add_review(self, movie:Movie, score:int) -> bool:
        try:
            if score > 10 or score < 1 or isinstance(score,float):
                raise Exception('Invalid Rating! Rating range: 1-10')
        except Exception as e:
            print(e)
            return False # Unsuccessful
            
        try: 
            if movie.name in self.rated_movies:
                raise Exception('One movie cannot be rated multiple times. Sorry!') # Report back movie already rated
        except Exception as e:
            print(e)
            return False # Unsuccessful

        try:
            if movie.year_published >= datetime.datetime.now().year:
                raise Exception('Movie not released yet. Sorry!') # UpComing Movie Exception
        except Exception as e:
            print(e)
            return False # Unsuccessful

        movie.no_of_reviews += 1
        self.rated_movies.add(movie.name)
        self.role = self.role.calc_score(movie, score, len(self.rated_movies))
        return True # Success