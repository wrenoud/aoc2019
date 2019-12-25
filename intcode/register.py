from typing import List


class Register(object):
    def __init__(self, address: int, memory: List[int]):
        self.address = address
        self.memory = memory

    def _memcheck(self):
        memsize = len(self.memory)
        if self.address >= memsize:
            grow = self.address - memsize + 1
            for i in range(grow):
                self.memory.append(0)

    @property
    def value(self) -> int:
        self._memcheck()
        return self.memory[self.address]

    @value.setter
    def value(self, value: int):
        self._memcheck()
        self.memory[self.address] = value

    def seek(self, value: int, absolute: bool = False):
        if absolute:
            self.address = value
        else:
            self.address += value

    def valid(self) -> bool:
        return -1 < self.address < len(self.memory)

    def __repr__(self) -> str:
        return f"Memory[@{self.address}] = {self.value}"
