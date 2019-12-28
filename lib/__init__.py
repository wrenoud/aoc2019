

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


class Maze(object):
    def __init__(self, maze):
        self.maze = maze

    @property
    def width(self):
        return len(self.maze[0])

    @property
    def height(self):
        return len(self.maze)

    def cell(self, x, y=None):
        if isinstance(x, Coord):
            return self.maze[x.y][x.x]
        return self.maze[y][x]

    def adjacent(self, position: Coord, exclude=None):
        opendirs = []
        for position in (
            Coord(position.x, position.y - 1),
            Coord(position.x, position.y + 1),
            Coord(position.x - 1, position.y),
            Coord(position.x + 1, position.y),
        ):
            v = self.cell(position)
            if exclude is None or v not in exclude:
                opendirs.append((position, v))

        return opendirs

    def iter(self):
        """this assumes maze boundaries and does not include them"""
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                yield (Coord(x, y), self.cell(x, y))
