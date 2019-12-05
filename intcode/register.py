class Register(object):
    def __init__(self, address, memory):
        self.address = address
        self.memory = memory

    @property
    def value(self) -> int:
        return self.memory[self.address]

    @value.setter
    def value(self, value: int):
        self.memory[self.address] = value

    def seek(self, value: int, absolute: bool = False):
        if absolute:
            self.address = value
        else:
            self.address += value

    def valid(self):
        return -1 < self.address < len(self.memory)

    def __repr__(self):
        return f"Memory[@{self.address}] = {self.value}"
