from mypy_extensions import TypedDict

Movie = TypedDict('Movie', {'name': str, 'year': int})
blade_runner: Movie = {'name': 'Blade Runner', 'year': 1982}
toy_story = Movie(name='Toy Story', year=1995)
