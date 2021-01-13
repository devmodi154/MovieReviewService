import os
from Handler import Handler

class InputStructures():
    def __init__(self,dataDir):
        self.dataDir = dataDir
        self.handler = Handler()
    
    def readTextFile(self,filename):
        with open(self.dataDir+"/"+filename,"r") as f:
            textData = []
            for lines in f:
                lines = lines.replace("\n","")
                textData.append(lines)
        return textData
	
    def initMovieData(self,filename):
        moviesRawData = self.readTextFile(filename)
        for movie in moviesRawData:
            movie = movie.split(",")
            self.handler.add_movie(movie[0], int(movie[1]), movie[2])

    def initUserData(self,filename):
        usersRawData = self.readTextFile(filename)
        for user in usersRawData:
            self.handler.add_user(str(user))

    def initReviewData(self,filename):
        reviewsRawData = self.readTextFile(filename)
        for review in reviewsRawData:
            review = review.split(",")
            self.handler.add_review(review[0], review[1], int(review[2]))


    def setup(self, moviesFilename, usersFilename, reviewsFilename):
        self.initMovieData(moviesFilename)
        self.initUserData(usersFilename)
        self.initReviewData(reviewsFilename)
        return self.handler



def dataInit():
    ''' 
    Function to return initial users and movies with added reviews.
    '''
    dirname = os.path.dirname(__file__)
    dataPath = os.path.join(dirname, 'data')
    input = InputStructures(dataPath)
    handler = input.setup("movies.txt","users.txt","reviews.txt")	
    return handler.movies, handler.users