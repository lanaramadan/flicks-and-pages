"""
This module deals with generating movies that match the user's taste in books
It utilizes Kaggle's TMDB 5000 Movie Dataset 
"""
import pandas as pd
import numpy as np
from flask import Flask
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import movie_api

class Movie():
    movie_recs = {}
    def __init__(self, book_title, movie_title, description, image):
        self.book_title = book_title
        self.movie_title = movie_title
        self.description = description
        self.image = image

def generate_movies(movie_data, book_description):
    """Generates and returns 4 movies (and descriptions) based on the cosine similarity with the book description"""

    # clean movie descriptions
    tfidf = TfidfVectorizer(stop_words="english")
    movie_data['overview'] = movie_data['overview'].fillna("")  # fills missing values

    # transform movie and book descriptions
    book_vector = tfidf.fit_transform([book_description])
    movie_matrix = tfidf.transform(movie_data['overview'])

    # calculate cosine similarity
    cos_similarity = cosine_similarity(movie_matrix, book_vector)

    # find movies with highest cosine similarity
    similar_movies = [(index, item) for index, item in enumerate(cos_similarity) if item > .2]
    top_four_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[0:4]

    # returns the movie name and movie description based on the index
    return [(movie_data['original_title'].iloc[[movie[0]]].item(),  movie_data['overview'].iloc[[movie[0]]].item()) for movie in top_four_movies]


def get_movies(book_name, movie_data, book_description):
    """Calls the generate function and returns a list of movies that match the book"""
    movies = generate_movies(movie_data, book_description)
    Movie.movie_recs[book_name] = []
    for movie in movies:
        movie_object = Movie(book_title = book_name, movie_title = movie[0], description = movie[1], image = movie_api.get_movie_image(movie[0]))
        Movie.movie_recs[book_name].append(movie_object)

    return Movie.movie_recs
