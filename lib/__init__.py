

class Coord(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __len__(self) -> int:
        """returns manhattan distance from origin"""
        return abs(self.x) + abs(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return "{}({},{})".format(self.__class__.__name__, self.x, self.y)


class Coord3D(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Coord3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Coord3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __len__(self) -> int:
        """returns manhattan distance from origin"""
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self) -> str:
        return "{}({},{},{})".format(self.__class__.__name__, self.x, self.y, self.z)
