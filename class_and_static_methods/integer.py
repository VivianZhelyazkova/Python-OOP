from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if float_value is not float:
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls,value):
        