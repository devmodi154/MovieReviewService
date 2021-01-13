from models.Review import Review


class Movie():
    def __init__(self, name:str, year_published:int, genre:str) -> None:
        self._name = name
        self._year_published = year_published
        self._genre = genre
        self._review_scores = Review() 
        self._no_of_reviews = 0

    # Setter Getters
    @property
    def name(self)->str:
        return self._name
    @name.setter
    def name(self, value)->None:
        self._name = value

    @property
    def year_published(self)->int:
        return self._year_published
    @year_published.setter
    def year_published(self, value)->None:
        self._year_published = value

    @property
    def genre(self)->str:
        return self._genre
    @genre.setter
    def genre(self, value)->None:
        self._genre = value

    @property
    def review_scores(self)->Review:
        return self._review_scores
    @review_scores.setter
    def review_scores(self, value)->None:
        self._review_scores = value

    @property
    def no_of_reviews(self)->int:
        return self._no_of_reviews
    @no_of_reviews.setter
    def no_of_reviews(self, value)->None:
        self._no_of_reviews = value
    # Setter Getters End

    # Dunder for CLI
    def __repr__(self):
        return "Name: " + self.name + "\nYear Published: " + str(self.year_published) + "\nGenre: " + self.genre + '\nReviews:\n' + str(self.review_scores)
    