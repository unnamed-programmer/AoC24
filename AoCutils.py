from enum import Enum

class Vector2():
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y + other.y, self.x + other.x)
        elif isinstance(other, int):
            return Vector2(self.y + other, self.x + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y - other.y, self.x - other.x)
        elif isinstance(other, int):
            return Vector2(self.y - other, self.x - other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__add__(0 - other)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y * other.y, self.x * other.x)
        elif isinstance(other, int):
            return Vector2(self.y * other, self.x * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y / other.y, self.x / other.x)
        elif isinstance(other, int):
            return Vector2(self.y / other, self.x / other)
        else:
            return NotImplemented

    def __rdiv__(self, other):
        return self.__div__(other)

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return True if self.x == other.x and self.y == other.y else False
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Vector2):
            return False if self.x == other.x and self.y == other.y else True
        else:
            return True

    def __iter__(self):
        yield self.y
        yield self.x

    def __repr__(self):
        return f"Vector2({self.y}, {self.x})"

    def __print__(self):
        return f"{self.y}, {self.x}"

    def __hash__(self):
        return hash((self.y, self.x))

class dr(Enum): # direction
    up =    0
    right = 1
    down =  2
    left =  3

drVec = [
    Vector2(-1, 0),
    Vector2(0 , 1),
    Vector2(1 , 0),
    Vector2(0 ,-1),
]

if __name__ == "__main__":
    print('This is a library.')