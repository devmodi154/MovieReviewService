# Movie Review Service
A simple service in python for adding users and movies with the functionality of users being capable of reviewing movies.

## Directory Structure
<img src="https://i.imgur.com/wX58lcj.png" alt="Directory structure">
- Data directory includes txt files with data(in list with each element in the next line) in the following format:
    - movies.txt: <movie_name>,<year_published>,<genre> 
    - users.txt: <user_name> 
    - reviews.txt: <user_name>,<movie_name>,<score> 
- Models contain the properties and inner working of each class.
- dataInput works for inputting data from text files for returning users and movies objects.
- Handler class operates on each query like adding users/movies, retrieve movies, and average scores. 
- Main.py is the runner for a sample case for which data is loaded in the text files.

## Run
Alter the data in text files in data/ directory.
- Download repository.
    `cd <repo-folder-name>`
    `python3 Main.py`

## Test:
Alter the data in tests/testHandler.py file -> load_data function for conducting tests.
`python3 -m tests.testHandler`
