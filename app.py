from flask import Flask, render_template, url_for, request, redirect
import book2movie

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def generate():
    if request.method == "POST":
        # if "generate recommendations" button is clicked, load the results page
        book_name = request.form['book-name'].title()
        movies = book2movie.get_movies(book_name)
        return render_template('results.html', book_name=book_name, movies=movies)
    else:
        # otherwise, load the home page
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
