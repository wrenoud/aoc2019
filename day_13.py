import util
from intcode import computer, format_program
from lib import Coord
from copy import copy
from time import sleep
from os import system

from day_11 import Canvas


class Arcade(object):
    def __init__(self, program):
        program[0] = 2 # enable free play

        self.canvas = Canvas({0:' ', 1:'#', 2:'X', 3:'T', 4:'O'}, False)
        self.segment = 0
        self.stdout = computer.Run(program, self.joystick())
        self.ball = None
        self.paddle = None

    def joystick(self):
        while True:
            system('cls')

            print(self.canvas)
            print(self.segment)
            
            if self.paddle.x < self.ball.x:
                yield 1
            elif self.paddle.x > self.ball.x:
                yield -1
            else:
                yield 0

    def play(self):
        while True:
            try:
                pos = Coord(next(self.stdout), next(self.stdout))
                value = next(self.stdout)
            except StopIteration:
                return

            if pos.x == -1:
                self.segment = value
            else:
                if value == 3:
                    self.paddle = pos
                elif value == 4:
                    self.ball = pos
                self.canvas.paint(pos, value)


def part1(program):
    stdout = computer.Run(program, None)

    canvas = Canvas({0:' ', 1:'#', 2:'X', 3:'T', 4:'O'}, False)
    while True:
        try:
            pos = Coord(next(stdout), next(stdout))
            tile = next(stdout)
        except StopIteration:
            break

        canvas.paint(pos, tile)

    print(canvas)
    util.Answer(1, sum(1 for v in canvas.canvas.values() if v == 2))

        
def part2(program):

    arcade = Arcade(program)
    arcade.play()
    util.Answer(2, arcade.segment)


if __name__ == "__main__":
    data = format_program(util.ReadPuzzle())

    part1(copy(data))
    part2(copy(data))
