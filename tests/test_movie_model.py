from src.models import Movie

def test_movie_model():
    movie = Movie(title='Star Wars', director='George Lucas', rating=5)

    assert type(movie) == Movie
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 5
