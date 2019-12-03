import util


class Opcode:
	def __init__(self, params, command):
		self.params = params
		self.command = command

	def Execute(self, cursor, memory):
		self.command(*memory[cursor + 1:cursor + 1 + self.params], memory)
		return self.params + 1


def opcode_1(a, b, c, m):
	m[c] = m[a] + m[b]


def opcode_2(a, b, c, m):
	m[c] = m[a] * m[b]


opcodes = {
	1: Opcode(3, opcode_1),
	2: Opcode(3, opcode_2),
}


def ExecuteIntcode(program):
	memory = program[:]
	cursor = 0
	opcode = memory[cursor]
	while opcode != 99:
		if opcode in opcodes:
			cursor += opcodes[opcode].Execute(cursor, memory)
			opcode = memory[cursor]
		else:
			print('Bad opcode {} at address {}')
			break
	return memory[0]


def test(code, register0):
	assert ExecuteIntcode(code) == register0


def part1(data):
	test([1, 1, 1, 4, 99, 5, 6, 0, 99], 30)
	test([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 3500)

	util.Answer(1, ExecuteIntcode(data))


def part2(data):
	for noun in range(100):
		for verb in range(100):
			data[1] = noun
			data[2] = verb
			if ExecuteIntcode(data) == 19690720:
				print(100 * noun + verb, noun, verb)

	util.Answer(2, None)


if __name__ == "__main__":
	data = util.ReadPuzzle()

	data = list(int(v) for v in data[0].split(','))
	data[1] = 12
	data[2] = 2

	part1(data)
	part2(data)

