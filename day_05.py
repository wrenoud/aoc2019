import util

from intcode import intcodemachine


def part1(data):
	program = data[:]
	ret = intcodemachine.Run(program, 1)
	util.Answer(1, ret)

		
def part2(data):
	program = data[:]
	ret = intcodemachine.Run(program, 5)
	util.Answer(2, ret)


if __name__ == "__main__":
	data = util.ReadPuzzle()
	data = list(int(v) for v in data[0].split(','))
	part1(data)
	part2(data)
