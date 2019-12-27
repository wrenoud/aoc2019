import util

from intcode import computer


def part1(data):
    program = data[:]
    stdout = computer.Run(program, 1)
    util.Answer(1, list(stdout)[-1])


def part2(data):
    program = data[:]
    stdout = computer.Run(program, 5)
    util.Answer(2, list(stdout)[-1])


if __name__ == "__main__":
    data = util.ReadPuzzle()
    data = list(int(v) for v in data[0].split(","))
    part1(data)
    part2(data)
