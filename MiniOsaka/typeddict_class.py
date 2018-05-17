from mypy_extensions import TypedDict

class Movie(TypedDict):
    name: str
    year: int

blade_runner: Movie = {'name': 'Blade Runner', 'year': 1982}

class ExtraMovie(Movie):
    director: str

the_rock = ExtraMovie(name='The Rock', year=1996, director='Michael Bay')

print(the_rock)
