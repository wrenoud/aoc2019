import util

from intcode import Memory, IntcodeMachine
from intcode.opcodes import Halt, Add, Multipy


machine = IntcodeMachine([Halt, Add, Multipy])

def part1(data):

	program = Memory([1, 1, 1, 4, 99, 5, 6, 0, 99])
	machine.Run(program)
	assert program.get(0) == 30

	program = Memory([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
	machine.Run(program)
	assert program.get(0) == 3500

	program = Memory(data[:])
	machine.Run(program)

	util.Answer(1, program.get(0))


def part2(data):
	for noun in range(100):
		for verb in range(100):
			program = Memory(data[:]) # make a copy
			program.set(1, noun)
			program.set(2, verb)

			machine.Run(program)
			if program.get(0) == 19690720:
				util.Answer(2, f"{100 * noun + verb} (noun: {noun}, verb: {verb})")
				break


if __name__ == "__main__":
	data = util.ReadPuzzle()

	data = list(int(v) for v in data[0].split(','))
	data[1] = 12
	data[2] = 2

	part1(data)
	part2(data)

