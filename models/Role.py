import abc
from models.Movie import Movie

class Role(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        self._role_threshold = 3
        self._score_weight_factor = 1

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'calc_score') and 
                callable(subclass.calc_score))


class Viewer(Role):
    def __init__(self) -> None:
        super().__init__()
    
    def calc_score(self, movie:Movie, score:int, no_of_user_ratings:int):
        # Update Score
        movie.review_scores.update_viewer_score(score)
        try:
            movie.review_scores._avg_review_score = movie.review_scores.get_total_score() / movie.no_of_reviews 
        except Exception as e:
            pass
        # Update role. Can be made a separate function if more roles are added.
        if no_of_user_ratings == self._role_threshold:
            return Critic()
        return self

class Critic(Role):
    def __init__(self) -> None:
        super().__init__()
        self._score_weight_factor = 2
    
    def calc_score(self, movie:Movie, score:int, no_of_user_ratings:int):
        # Update Score
        movie.review_scores.update_critic_score(score, self._score_weight_factor)
        try:
            movie.review_scores._avg_review_score = movie.review_scores.get_total_score() / movie.no_of_reviews
        except Exception as e:
            pass
        return self