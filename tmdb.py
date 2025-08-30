import os
import tmdbsimple as tmdb
from dotenv import load_dotenv

load_dotenv()
tmdb.API_KEY = os.getenv('API_KEY')

tmdb.REQUESTS_TIMEOUT = 5


def movie_info(movie_id):
    movie = tmdb.Movies(movie_id)

    worddict = movie.keywords()
    keywords = []

    for kw in worddict.get('keywords', []):
        keywords.append(kw["name"])

    return keywords


def search_movies(query):
    search = tmdb.Search()
    response = search.movie(query=query)

    movies = []
    for s in search.results:
        title = s.get('title', 'No Title')
        movie_id = s.get('id', None)
        release_date = s.get('release_date', 'Unknown')
        popularity = s.get('popularity', 0)

        movies.append({
            'title': title,
            'id': movie_id,
            'release_date': release_date,
            'popularity': popularity
        })

    return movies
