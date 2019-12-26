import util
from typing import Optional, List, Tuple
from lib import Coord


class Segment(object):
    def __init__(self, begin: Coord, end: Coord):
        assert begin.x == end.x or begin.y == end.y  # should be horizontal or vertical
        self.begin = begin
        self.end = end

    def min(self, dim: str) -> int:
        return min(self.begin.__getattribute__(dim), self.end.__getattribute__(dim))

    def max(self, dim: str) -> int:
        return max(self.begin.__getattribute__(dim), self.end.__getattribute__(dim))

    def orientation(self) -> bool:
        """returns true if horizontal, assumes only one axis varies"""
        return self.begin.x != self.end.x

    def intersects(self, other) -> Optional[Coord]:
        """returns None or Coord of intersection between self and other"""
        if self.orientation() == other.orientation():
            return None

        def intersection(horiSegment: Segment, vertSegment: Segment) -> Optional[Coord]:
            if horiSegment.min("x") <= vertSegment.begin.x <= horiSegment.max("x"):
                if vertSegment.min("y") <= horiSegment.begin.y <= vertSegment.max("y"):
                    if vertSegment.begin.x == 0 and horiSegment.begin.y == 0:
                        return None
                    return Coord(vertSegment.begin.x, horiSegment.begin.y)
            return None

        if self.orientation():  # self is horizontal
            return intersection(self, other)
        else:  # self is vertical
            return intersection(other, self)

    def __len__(self) -> int:
        return len(self.begin - self.end)

    def __repr__(self) -> str:
        return "{}({},{})".format(self.__class__.__name__, self.begin, self.end)


class PolyLine(object):
    def __init__(self, directions: List[Tuple[str, int]]):
        self.segments = []
        pos = Coord(0, 0)

        for direction, distance in directions:
            current = pos
            if direction == "R":
                pos += Coord(distance, 0)
            elif direction == "L":
                pos += Coord(-distance, 0)
            elif direction == "U":
                pos += Coord(0, distance)
            elif direction == "D":
                pos += Coord(0, -distance)
            self.segments.append(Segment(current, pos))

    def Intersect(self, other) -> List[Tuple[Coord, int]]:
        intersections = []
        wireLength = Coord(0, 0)  # x is self, y is other
        for selfSegment in self.segments:
            wireLength.y = 0
            for otherSegment in other.segments:
                intersection = selfSegment.intersects(otherSegment)
                if intersection is not None:
                    totalWireLength = (
                        len(wireLength)
                        + len(
                            intersection - selfSegment.begin
                        )  # additional length on self wire
                        + len(
                            intersection - otherSegment.begin
                        )  # additional length on other wire
                    )
                    intersections.append((intersection, totalWireLength))
                wireLength.y += len(otherSegment)
            wireLength.x += len(selfSegment)
        return intersections


def part1(data):
    p1 = PolyLine(data[0])
    p2 = PolyLine(data[1])

    util.Answer(1, min(len(c) for c, d in p1.Intersect(p2)))


def part2(data):
    p1 = PolyLine(data[0])
    p2 = PolyLine(data[1])

    util.Answer(2, min(d for c, d in p1.Intersect(p2)))


if __name__ == "__main__":
    data = util.ReadPuzzle()

    def format_input(data):
        return list((v[:1], int(v[1:])) for v in data.split(","))

    # test data
    p1 = PolyLine(format_input("R8,U5,L5,D3"))
    p2 = PolyLine(format_input("U7,R6,D4,L4"))
    assert min(len(c) for c, d in p1.Intersect(p2)) == 6
    assert min(d for c, d in p1.Intersect(p2)) == 30

    p1 = PolyLine(format_input("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"))
    p2 = PolyLine(format_input("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))
    assert min(len(c) for c, d in p1.Intersect(p2)) == 135
    assert min(d for c, d in p1.Intersect(p2)) == 410

    # massage the data into tuples of the direction character
    # and the distance as an int
    data = [format_input(data[0]), format_input(data[1])]

    part1(data)
    part2(data)
