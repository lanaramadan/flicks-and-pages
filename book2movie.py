class Movie():
    movie_recs = {"Test": [1, 2, 3]}
    def __init__(title):
        # define poster, description, title, and link?
        self.title = title
        Movie.movie_recs[self.title].append(self)

def generate_movies(book_name):
    """Generates 4 movies based on the book name"""
    pass

def get_movies(book_name):
    """Calls the generate function and returns a list of movies that match the book"""
    generate_movies(book_name)
    try:
        return Movie.movie_recs[book_name]
    except KeyError:
        return []