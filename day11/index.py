from collections import defaultdict, namedtuple
import csv
from urllib.request import urlretrieve
import ssl

# Чисто для загрузки файла
ssl._create_default_https_context = ssl._create_unverified_context
movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
# Запрашивает файл и кладёт по имени
urlretrieve(movie_data, movies_csv)

MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', ['title', 'year', 'score'])

def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    directors = defaultdict(list)

    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                title = line['movie_title']
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            if year >= MIN_YEAR:
                m = Movie(title, year, score)
                directors[director].append(m)
    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    sum_score = 0
    for movie in movies:
        sum_score += movie.score
    
    return round(sum_score / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    result = []
    for k, v in directors.items():
        if len(v) < MIN_MOVIES:
            continue
        result.append((k, calc_mean_score(v)))
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result