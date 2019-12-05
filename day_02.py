import util

from intcode import computer


def part1(data):

	program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
	computer.Run(program)
	assert program[0] == 30

	program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
	computer.Run(program)
	assert program[0] == 3500

	program = data[:]
	computer.Run(program)

	util.Answer(1, program[0])


def part2(data):
	for noun in range(100):
		for verb in range(100):
			program = data[:] # make a copy
			program[1] = noun
			program[2] = verb

			computer.Run(program)
			if program[0] == 19690720:
				util.Answer(2, f"{100 * noun + verb} (noun: {noun}, verb: {verb})")
				break


if __name__ == "__main__":
	data = util.ReadPuzzle()

	data = list(int(v) for v in data[0].split(','))
	data[1] = 12
	data[2] = 2

	part1(data)
	part2(data)

