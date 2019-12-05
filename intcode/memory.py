class Memory(object):
    def __init__(self, memory):
        self.memory = memory

    def get(self, address: int):
        return self.memory[address]

    def set(self, address: int, value: int):
        self.memory[address] = value


class Register(object):
    def __init__(self, address, memory):
        self.address = address
        self.memory = memory

    @property
    def value(self) -> int:
        return self.memory.get(self.address)

    @value.setter
    def value(self, value: int):
        self.memory.set(self.address, value)

    def __repr__(self):
        return f"Memory[@{self.address}] = {self.value}"


class MemoryWalker(object):
    def __init__(self, memory: Memory):
        self.memory = memory
        self.cursor = 0

    def reset(self):
        self.cursor = 0

    def next(self) -> Register:
        register = Register(self.cursor, self.memory)
        self.cursor += 1
        return register
