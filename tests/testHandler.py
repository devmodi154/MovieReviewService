from models.Role import Critic
from Handler import Handler
from dataInput import dataInit
import unittest

class testHandler(unittest.TestCase):
    def setUp(self):
        self.movies = {}
        self.users = {}
    # Use text files under data directory
        # self.movies, self.users = dataInit() # If using this, then comment remaining function
    
    # Directly  loading input data 
        self.handler = Handler(self.movies, self.users)   
        self.load_data()     

    # EXCEPTION TESTS
    def test_rating_upcoming_movie(self):
        self.assertEqual(False, self.handler.add_review('Deepika','Lunchbox',5))

    def test_one_user_rating_multiple_times(self):
        self.assertEqual(False, self.handler.add_review('SRK','Don',1))
    
    def test_viewer_role_update(self):
        # While loading data the user SRK became a Critic
        self.assertEqual(True, isinstance(self.handler.users['SRK'].role,Critic))
    
    def test_critic_score_weight(self):
        self.handler.add_review('SRK','Metro',7)
        self.assertEqual(14, self.handler.movies['Metro'].review_scores.critic_score)


    # QUERY TESTS
    def test_query_movie_viewer_score_by_year(self):
        results = self.handler.retrieve(limit=1,year_published=2006)
        self.assertEqual(16, results[0].review_scores.viewer_score)

    def test_query_movie_critic_score_by_year(self):
        results = self.handler.retrieve(limit=1,role='c',year_published=2006)
        self.assertEqual(14, results[0].review_scores.critic_score)
    
    def test_query_movie_by_genre(self):
        results = self.handler.retrieve(limit=1,genre='drama')
        self.assertEqual((6,'Guru'), (results[0].review_scores.viewer_score,results[0].name))
    
    def test_query_movie_avg_score_by_year(self):
        results = self.handler.retrieve_avg_score(year_published=2006)
        self.assertEqual(7.33,round(results,2))   
    
    def load_data(self):
        # Adding movies
        self.handler.add_movie('Don',2006,'Action')
        self.handler.add_movie('Tiger',2008,'Drama')
        self.handler.add_movie('Padmavaat',2006,'Comedy')
        self.handler.add_movie('Lunchbox',2021,'Drama')
        self.handler.add_movie('Guru',2006,'Drama')
        self.handler.add_movie('Metro',2006,'Romance')
        
        # Adding users
        self.handler.add_user('SRK')
        self.handler.add_user('Salman')
        self.handler.add_user('Deepika')

        # Adding reviews
        self.handler.add_review('SRK','Don',2)
        self.handler.add_review('SRK','Padmavaat',8)
        self.handler.add_review('Salman','Don',5)
        self.handler.add_review('Deepika','Don',9)
        self.handler.add_review('Deepika','Guru',6)
        self.handler.add_review('SRK','Tiger',5)
        self.handler.add_review('SRK','Metro',7)


if __name__ == "__main__":
    unittest.main()


