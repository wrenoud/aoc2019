from intcode.register import Register


class State(object):
	def __init__(self, memory, stdin, verbose: bool):
		self.memory = memory
		self.cursor = Register(0, self.memory) # Register
		self.stdin = stdin # generator
		self.verbose = verbose
		self.relativebase = 0
