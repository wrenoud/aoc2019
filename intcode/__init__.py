from typing import List

from intcode.exceptions import ProgramHalt
from intcode.opcodes import BaseOpcode
from intcode.memory import Memory, Register, MemoryWalker

class Command(object):
    def __init__(self, command: int):
        # padd
        command = f"{command:05}"
        # extract
        self.code = command[-2:]
        self.modes = command[-3::-1]


class IntcodeMachine(object):
    def __init__(self, opcodes: List[BaseOpcode]):
        self.opcodes = {}
        for cls in opcodes:
            opcode = cls.code().zfill(2)  # ensure padding
            self.opcodes[opcode] = cls()

    def Run(self, memory: Memory, input=None):
        output = None
        walker = MemoryWalker(memory)
        while True:
            commandregister = walker.next()
            command = Command(commandregister.value)
            if command.code not in self.opcodes:
                raise Exception(f"Bad Opcode {command.code} ({commandregister})")

            opcode = self.opcodes[command.code]

            # read parameters from memory and act on parameter mode
            parameters = []
            for i in range(opcode.parametercount()):
                register = walker.next()
                if (command.modes[i]) == "0":  # position mode
                    # interpret parameter as memory address to read
                    parameters.append(Register(register.value, memory))
                if (command.modes[i]) == "1":  # immediate mode
                    # interpret parameter as value
                    parameters.append(register)

            # execute opcode
            try:
                ret = opcode(memory, input, parameters)
                if ret is not None:
                    output = ret
            except ProgramHalt:
                break
        return output
