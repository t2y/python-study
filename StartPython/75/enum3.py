from enum import Enum, EnumMeta, _EnumDict

class EnumDefaultDict(_EnumDict):
    def __missing__(self, key):
        self[key] = 1

class ImplicitEnumMeta(EnumMeta):
    @classmethod
    def __prepare__(metacls, cls, bases):
        return EnumDefaultDict()

class ImplicitEnum(Enum, metaclass=ImplicitEnumMeta):
    pass

class Color(ImplicitEnum):
    RED
    GREEN
    BLUE
