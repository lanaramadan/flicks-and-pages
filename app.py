from flask import Flask, render_template, url_for, request, redirect
import os
import pandas as pd
import book2movie, book_api

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


        return render_template('results.html', book_name=book_name, movies=movies)
    else:
        # otherwise, load the home page
        return render_template('index.html')


if __name__ == "__main__":
    movie_data = get_movie_data()
    description = book_api.get_book_description("Dune".replace(" ", "+"))
    print(description)
    print(list(book2movie.get_movies("Dune", get_movie_data(), description)))
    # app.run(debug=True)
