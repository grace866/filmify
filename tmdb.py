import tmdbsimple as tmdb

tmdb.API_KEY = 'b1b74485fb7b95abcebdbc748776c51c'
tmdb.REQUESTS_TIMEOUT = 5


def movie_info(movies):
    for movie in movies:
        movie_id = movie['id']

        movie = tmdb.Movies(movie_id)
        details = movie.info()

        genres = details.get('genres', [])
        keywords = details.get('keywords', [])

        return (genres, keywords)


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
