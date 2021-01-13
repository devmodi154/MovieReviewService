from Handler import Handler
from dataInput import dataInit


def main():
    movies, users = dataInit() # From data in text files
    handler = Handler(movies, users)
    results = handler.retrieve(limit=1,role='c',year_published=2006)
    results = handler.retrieve_avg_score(year_published=2006)
    # print(results)
    for movie in results:
        print(movie)
        print()

if __name__ == "__main__":
    main()