"""
This module deals with generating movies that match the user's taste in books
It utilizes Kaggle's TMDB 5000 Movie Dataset 
"""
import pandas as pd
import numpy as np
from flask import Flask
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

class Movie():
    movie_recs = {}
    def __init__(self, title):
        # define poster, description, title, and link?
        self.title = title
        self.description = "hello"
        Movie.movie_recs[self.title].append(self)

def generate_movies(book_name, movie_data, book_description):
    """Generates and returns 4 movies based on the book name"""
    # TODO: generate each movie and each time Movie.movie_recs[book_name].append(Movie(title, blah, blah))

    tfidf = TfidfVectorizer(stop_words="english")
    movie_data['overview'] = movie_data['overview'].fillna("")  # fills missing values
    movie_matrix = tfidf.fit_transform(movie_data['overview'])
    # cos_similarity = cosine_similarity(movie_matrix, movie_matrix)
    # print("COS:", cos_similarity)
    # return Movie.movie_recs[book_name]

def get_movies(book_name, movie_data, book_description):
    """Calls the generate function and returns a list of movies that match the book"""
    # generate_movies(book_name)
    try:
        return generate_movies(book_name, movie_data, book_description)
    except KeyError:
        return []
    
