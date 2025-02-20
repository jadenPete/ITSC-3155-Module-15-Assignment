import pytest
from src.repositories import movie_repository

@pytest.mark.usefixtures("clear_movie_repository")
def test_movie_model():
    allMovie = movie_repository.movie_repository_singleton

    assert len(allMovie.get_all_movies()) == 0

    allMovie.create_movie("Avatar", "Director1", 4)
    allMovie.create_movie("Fast and Furious", "Director2", 1)
    allMovie.create_movie("Smile", "Director3", 2)

    assert len(allMovie.get_all_movies()) != 0
