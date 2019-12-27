import util
from intcode import computer
from lib import Coord
from copy import copy

BLACK = 0
WHITE = 1


class Canvas(object):
    def __init__(self, colormap={BLACK: " ", WHITE: "#"}, inverted=True):
        self.canvas = {}
        self.colormap = colormap
        self.inverted = inverted

    def paint(self, position: Coord, color: int):
        self.canvas[position] = color

    def color(self, position: Coord):
        if position in self.canvas:
            return self.canvas[position]
        else:
            return None

    def __repr__(self):
        mins = Coord(0, 0)
        maxs = Coord(0, 0)
        for key in self.canvas.keys():
            mins.x = min(key.x, mins.x)
            mins.y = min(key.y, mins.y)
            maxs.x = max(key.x, maxs.x)
            maxs.y = max(key.y, maxs.y)

        canvas = []
        for i in range(maxs.y - mins.y + 1):
            canvas.append([".",] * (maxs.x - mins.x + 1))

        for key, color in self.canvas.items():
            pos = key - mins
            canvas[pos.y][pos.x] = self.colormap[color]

        if self.inverted:
            canvas.reverse()

        return "\n".join("".join(str(v) for v in line) for line in canvas)


class Robot(object):
    def __init__(self, program, verbose=False):
        self.position = Coord(0, 0)
        self.direction = 0
        self.hull = Canvas()
        # pass the camera generator as stdin to the program
        self.stdout = computer.Run(program[:], self.Camera(), verbose)

    def Camera(self):
        while True:
            color = self.hull.color(self.position)
            if color is None:
                yield BLACK  # assume black if unpainted
            else:
                yield color

    def Paint(self):
        while True:
            try:
                color = next(self.stdout)
                rotation = next(self.stdout)
            except StopIteration:
                return

            position = copy(self.position)
            self.hull.paint(position, color)

            # execute turn
            if rotation:
                self.direction += 1
            else:
                self.direction -= 1
            self.direction %= 4

            # advance robot
            if self.direction == 0:
                self.position.y += 1
            elif self.direction == 1:
                self.position.x += 1
            elif self.direction == 2:
                self.position.y -= 1
            elif self.direction == 3:
                self.position.x -= 1

            yield (color, position)


def part1(data):
    # test job
    robot = Robot([], False)
    # replace the stdout from the program with a preplanned route
    robot.stdout = (
        v
        for v in [
            WHITE,
            0,  #
            BLACK,
            0,  #
            WHITE,
            0,  #
            WHITE,
            0,  #
            BLACK,
            1,  #
            WHITE,
            0,  #
            WHITE,
            0,
        ]
    )
    # we have to manually advance the camera output as no program will be asking for input
    camera = robot.Camera()
    for color, position in robot.Paint():
        next(camera)
    print(robot.hull)

    # actual paint job
    robot = Robot(data, False)
    for color, position in robot.Paint():
        pass

    util.Answer(1, len(robot.hull.canvas.keys()))


def part2(data):
    robot = Robot(data, False)

    # robot expects to start on a white panel
    robot.hull.paint(Coord(0, 0), WHITE)

    for color, position in robot.Paint():
        pass

    util.Answer(2, None)
    print(robot.hull)


if __name__ == "__main__":
    data = util.ReadPuzzle()
    data = list(int(v) for v in data[0].split(","))

    part1(data)
    part2(data)
