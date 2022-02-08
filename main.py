from flask import Flask, jsonify
from utils import get_data, get_year, movie_children, movie_family, movie_adult, movie_drama, movie_search, actors

app = Flask(__name__)

@app.route('/')
def page_index():
    return "Что будем искать?"


@app.route('/movies/<name>')
def page_index1(name):
    result=get_data(name)
    data_movie = {"title": result[1],
          "country": result[2],
          "release_year": result[3],
          "genre": result[4],
          "description": result[5]
          }
    return data_movie


@app.route('/movies/year/<int:year1>/<int:year2>' )
def page_index2(year1, year2):
    results = get_year(year1,year2)
    data_years = []
    for result in results:
        data_movie = {"title": result[0], "release_year": result[1]}
        data_years.append(data_movie)
    return jsonify(data_years)


@app.route('/rating/children')
def page_children():
    results = movie_children()
    data_movie_children = []
    for result in results:
        data_movie = {"title": result[0], "rating": result[1], "description": result[2]}
        data_movie_children.append(data_movie)
    return jsonify(data_movie_children)


@app.route('/rating/family')
def page_family():
    results = movie_family()
    data_movie_family = []
    for result in results:
        data_movie = {"title": result[0], "rating": result[1], "description": result[2]}
        data_movie_family.append(data_movie)
    return jsonify(data_movie_family)


@app.route('/rating/adult')
def page_adult():
    results = movie_adult()
    data_movie_adult = []
    for result in results:
        data_movie = {"title": result[0], "rating": result[1], "description": result[2]}
        data_movie_adult.append(data_movie)
    return jsonify(data_movie_adult)


@app.route('/<genre>')
def page_genre(genre):
    results = movie_drama(genre)
    data_movie_genre = []
    for result in results:
        data_movie = {"title": result[0], "description": result[1]}
        data_movie_genre.append(data_movie)
    return jsonify(data_movie_genre)


@app.route('/actors/<actors1>/<actors2>')
def page_actors(actors1, actors2):
    results = actors(actors1, actors2)
    return jsonify(list(results))


@app.route('/search/<type>/<int:year>/<genre>')
def page_search(type, year, genre):
    results = movie_search(type, year, genre)
    print(results)
    data_movie_search = []
    for result in results:
        data_movie = {"title": result[0], "description": result[1]}
        data_movie_search.append(data_movie)
    return jsonify(data_movie_search)

if __name__ == '__main__':
    app.run(debug=True)