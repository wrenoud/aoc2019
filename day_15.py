import util
from intcode import computer, format_program
from copy import copy
import msvcrt
from os import system
from lib import Coord
from day_11 import Canvas


class Robot(object):
    def __init__(self, program):
        self.canvas = Canvas({0:' ',1:'^',2:'V',3:'<',4:'>',5:'#'}, True)
        self.position = Coord(0,0)
        self.direction = 1
        self.stdout = computer.Run(program, self.stdin())
        self.distance = 0

    def stdin(self):
        while True:
            system('cls')
            print(self.canvas)
            print(self.distance)
            direction = msvcrt.getch()
            if direction == b'w':
                self.direction = 1
            elif direction == b's':
                self.direction = 2
            elif direction == b'a':
                self.direction = 3
            elif direction == b'd':
                self.direction = 4
            elif direction == b'\x03':
                exit()

            yield self.direction

    def run(self):
        while True:
            try:
                status = next(self.stdout)
            except StopIteration:
                print("END")
                break

            self.canvas.paint(self.position, 0)

            if status == 0:
                if self.direction == 1:
                    self.canvas.paint(self.position + Coord( 0, 1), 5)
                elif self.direction == 2:
                    self.canvas.paint(self.position + Coord( 0,-1), 5)
                elif self.direction == 3:
                    self.canvas.paint(self.position + Coord(-1, 0), 5)
                elif self.direction == 4:
                    self.canvas.paint(self.position + Coord( 1, 0), 5)
            elif status == 1 or status == 2:
                self.distance += 1
                if self.direction == 1:
                    self.position += Coord( 0, 1)
                elif self.direction == 2:
                    self.position += Coord( 0,-1)
                elif self.direction == 3:
                    self.position += Coord(-1, 0)
                elif self.direction == 4:
                    self.position += Coord( 1, 0)
                if status == 2:
                    print('-'*80)
                    print("SUCCESS!!")
                    print('-'*80)

            self.canvas.paint(self.position, self.direction)

def part1(program):
    robot = Robot(program)
    robot.run()
    util.Answer(1, None)

        
def part2(data):
    puzzle = [
        "#########################################",
        "#       #         #         #   #     # #",
        "# ### ### # ##### # ####### ### # # # # #",
        "#   # #   #   #   #   #   #   #   # #   #",
        "### # # ##### ### ### ### ### ##### ### #",
        "#   # #   # #   #   #   #     #     #O  #",
        "# ####### # ### # ##### # ##### ####### #",
        "# #   #       # # #     #     # #     # #",
        "# # # # ####### # # ######### # # ### # #",
        "# # #     #     # # # #       #   # # # #",
        "# # ####### ##### # # # ####### ### # # #",
        "#   #     # #     # #   #     #     # # #",
        "# ### ### # # ##### # ### # ##### ### # #",
        "#   # # # # #   #   #   # # #     #   # #",
        "### # # # # ### # ##### # # # ##### ### #",
        "#   # # # # #   # #   # # #       # #   #",
        "# ### # # # # ### # ### # ######### # ###",
        "# # # #   # # # # #   # #   #       # # #",
        "# # # # ### # # # ### # ##### ####### # #",
        "# # # #   # #   #   #     #   #   #   # #",
        "# # # ### # ####### ##### # ### # # ### #",
        "#   # # # #       # # #   #   # #   #   #",
        "### # # # ####### # # # ### # ##### # # #",
        "#   # #         # # # # #   #     #   # #",
        "# ### ######### # # # # ### ##### ##### #",
        "#   #   # #   # # #   #   #     # #   # #",
        "### ### # # # # # ####### ##### # # # # #",
        "#     # #   #           #     # #   # # #",
        "# ##### ############### ##### ####### # #",
        "# #   #         #   # # #   # #   #   # #",
        "### # ######### # # # # # # # # # # #####",
        "#   #           # # # # # # #   # # #   #",
        "# ### ########### # # # # # ##### # # # #",
        "# #   #           # #   # #     # #   # #",
        "# ##### ########### # ### ##### # ##### #",
        "# #     #         # #   # # #   # #   # #",
        "# # ####### ##### # ##### # # ### # # # #",
        "#   #       #   # # #   # # # #   # #   #",
        "# ####### ### ### # # # # # # # ### ### #",
        "#         #       #   #     #       #   #",
        "#########################################",
    ]
    util.Answer(2, None)


if __name__ == "__main__":
    data = format_program(util.ReadPuzzle())
    part1(copy(data))
    part2(copy(data))
