from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items = []  # type: List[T]

    def push(self, item: T) -> None:
        self.items.append(item)

stack = Stack[int]()
stack.push(1)
stack.push(2)
print(stack.items)
