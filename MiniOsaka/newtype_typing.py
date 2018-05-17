from typing import NewType

UserId = NewType('UserId', int)

def name_by_id(user_id: UserId) -> str:
    ...

UserId('user')          # error: Argument 1 to "UserId" has incompatible type "str"; expected "int"

name_by_id(42)          # error: Argument 1 to "name_by_id" has incompatible type "int"; expected "UserId"
name_by_id(UserId(42))  # OK

num = UserId(5) + 1     # type: int
