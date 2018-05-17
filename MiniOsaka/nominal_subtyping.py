from typing import Sized, Iterable, Iterator

class Bucket(Sized, Iterable[int]):

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...

result: int = collect(Bucket())  # Passes type check
