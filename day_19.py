import util
from copy import copy
from intcode import computer, format_program

from lib import Coord
from day_11 import Canvas


def stdin(coord):
        yield coord.x
        yield coord.y


def part1(data):
    coords = []
    effects = []
    canvas = Canvas({0: " ", 1: "#"}, inverted=False)
    for x in range(50):
        for y in range(50):
            coord = Coord(x, y)
            stdout = computer.Run(data[:], stdin(coord))
            coords.append(coord)
            effects.append(next(stdout))

            canvas.paint(coord, effects[-1])
        print(x)
    zip(coords, effects)

    util.Answer(1, sum(effects))

    print(canvas)

def part2(data):
    util.Answer(2, None)


if __name__ == "__main__":
    data = format_program(util.ReadPuzzle())
    part1(copy(data))
    part2(copy(data))
