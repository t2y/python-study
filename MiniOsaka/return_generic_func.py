from typing import TypeVar, Callable, Any, cast 

T = TypeVar('T', bound=Callable[..., Any])

def logged(description: str) -> Callable[[T], T]:
    def decorator(f: T) -> T:
        def wrapper(*args, **kwargs):
            print('entering:', description)
            value = f(*args, **kwargs)
            print('leaving:', description)
        return cast(T, wrapper)
    return decorator

@logged('system initialization')
def init() -> None:
    print('do something')

init(1)  # Too many arguments (signature is correctly preserved)
