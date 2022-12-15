from app import app
import pytest
from src.repositories.movie_repository import movie_repository_singleton

@pytest.fixture
def clear_movie_repository(test_app):
	with app.app_context():
		movie_repository_singleton.clear()

		yield

@pytest.fixture(scope='module')
def test_app():
    return app.test_client()
