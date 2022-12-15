import pytest
from src.models import Movie
from src.repositories.movie_repository import movie_repository_singleton

@pytest.mark.usefixtures("clear_movie_repository")
def test_movie_created():
    movie_repository = movie_repository_singleton
    movie_repository.create_movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)

    all_movies = movie_repository.get_all_movies()

    test_movie = Movie(title="Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", director="Larry Charles", rating=5)

    same_movie = False

    for movie in all_movies:
        if (movie.title, movie.director, movie.rating) == \
            (test_movie.title, test_movie.director, test_movie.rating):
            same_movie = True

    assert same_movie

@pytest.mark.usefixtures("clear_movie_repository")
def test_movie_not_created():
    movie_repository = movie_repository_singleton
    movie_repository.create_movie("Borat! Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan", "Larry Charles", 5)

    all_movies = movie_repository.get_all_movies()

    test_movie = Movie(title="Inception", director="Christopher Nolan", rating=5)

    same_movie = False

    for movie in all_movies:
        if (movie.title, movie.director, movie.rating) == \
            (test_movie.title, test_movie.director, test_movie.rating):
            same_movie = True

    assert not same_movie
