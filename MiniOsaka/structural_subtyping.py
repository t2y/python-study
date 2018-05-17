from typing import Iterator, Iterable

class Bucket:

    def __len__(self) -> int: ...

    def __iter__(self) -> Iterator[int]: ...

def collect(items: Iterable[int]) -> int: ...

result: int = collect(Bucket())  # Passes type check
