from models.Movie import Movie
from models.User import User


class Handler():
    def __init__(self, movies=dict(), users=dict()):
        self.movies = movies
        self.users = users

    def add_user(self, name:str)->User:
        self.users[name] = User(name)
        return self.users[name]
    
    def add_movie(self, name:str, year_published:int, genre:str)->Movie:
        self.movies[name] = Movie(name, year_published, genre)
        return self.movies[name]
    
    def add_review(self, user_name:str, movie_name:str, score:int)->bool:
        return self.users[user_name].add_review(self.movies[movie_name], score)
    
    def retrieve(self, limit = None, role = None, year_published = None, genre = None, desc = True):
        movies = list(self.movies.values())
        results = movies[:]
        if year_published:
            results = list(filter(lambda movie: movie.year_published == year_published, results))
        if genre:
            results = list(filter(lambda movie: movie.genre.lower() == genre.lower(), results))
        
        if not role or role.lower() == 'viewer' or role.lower() == 'v': # Viewer by default
            results.sort(key=lambda movie: movie.review_scores.viewer_score, reverse=desc)
        elif role.lower() == 'critic' or role.lower() == 'c':
            results.sort(key=lambda movie: movie.review_scores.critic_score, reverse=desc)
        if limit:
            return results[:limit]
        return results

    def retrieve_avg_score(self,movie_name=None, year_published=None, genre=None):
        movies = list(self.movies.values())
        results = movies[:]
        if movie_name:
            movie = self.movies[movie_name]
            return movie.review_scores.avg_review_score    
        if year_published:
            results = list(filter(lambda movie: movie.year_published == year_published, movies))
        if genre:
            results = list(filter(lambda movie: movie.genre.lower() == genre.lower(), results))
        
        total_score = sum(movie.review_scores.get_total_score() for movie in results)
        total_no_of_reviews = sum(movie.no_of_reviews for movie in results)
        try:
            result_score = total_score / total_no_of_reviews
        except Exception as e:
            print('No reviews')
            return 
        return result_score