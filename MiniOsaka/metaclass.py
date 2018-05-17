class Meta(type):
    def __add__(self, x: str) -> str: 
        return 'a' + x

class C(metaclass=Meta):
    ...

print(C + 'x')  # Okay
print(C + 1)  # error: Unsupported operand types for + ("Type[C]" and "int")
