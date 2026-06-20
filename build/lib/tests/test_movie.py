from index import Movie


def test_movie_creation():
    movie = Movie("Interstellar", "Nolan", 2014, 169, 9.5)

    assert movie.title == "Interstellar"
    assert movie.creator == "Nolan"
    assert movie.year == 2014
    assert movie.runtime == 169
    assert movie.rating == 9.5


def test_is_long_movie():
    movie = Movie("Interstellar", "Nolan", 2014, 169, 9.5)

    assert movie.is_long_movie() is True


def test_movie_recommend():
    movie = Movie("Interstellar", "Nolan", 2014, 169, 9.5)

    assert movie.recommend() is True