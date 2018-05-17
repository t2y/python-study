from mypy_extensions import TypedDict

Movie = TypedDict('Movie', {'name': str, 'year': int}, total=False)
the_rock = Movie(name='The Rock')

the_rock
the_rock['year']
