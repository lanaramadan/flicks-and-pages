from flask import Flask, render_template, url_for, request, redirect
import os
import pandas as pd
import book2movie, book_api


# TODO Display movie image by connecting to movie database
# TODO tranfer to heroku? https://www.youtube.com/watch?v=Z1RJmh_OqeA
# TODO replace kaggle with smth more accurate
# TODO loading images is really slow
app = Flask(__name__)

def get_movie_data():
    """Return the path to the file with the movie data"""
    root_path = app.root_path
    file_name = "tmdb_5000_movies.csv"
    file_path = os.path.join(root_path, "data", file_name)

    movie_data = pd.read_csv(file_path)

    return movie_data


@app.route('/', methods=['POST', 'GET'])
def generate():
    if request.method == "POST":
        # if "generate recommendations" button is clicked, load the results page
        book_name = request.form['book-name'].title().strip()
        book_description = book_api.get_book_description(book_name.replace(" ", "+"))

        movies = book2movie.get_movies(book_name, get_movie_data(), book_description)

        return render_template('results.html', book_name=book_name, movies=movies[book_name])
    else:
        # otherwise, load the home page
        return render_template('index.html')
    

@app.route('/results')
def back():
    # if "start a new search" button is clicked, load the home page
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
