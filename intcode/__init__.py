from typing import List
from copy import copy
from types import GeneratorType

from intcode.exceptions import ProgramHalt
from intcode.instructions import instructions
from intcode.register import Register


class Command(object):
    def __init__(self, command: int):
        # padd
        command = f"{command:05}"
        # extract
        self.opcode = command[-2:]
        self.modes = command[-3::-1]


class IntcodeComputer(object):
    def __init__(self, instructions: List):
        self.opcodes = {}
        for instruction in instructions:
            opcode = instruction.opcode.zfill(2)  # ensure padding
            assert opcode not in self.opcodes
            self.opcodes[opcode] = instruction

    def Run(self, memory: List[int], stdin=None, verbose=False):
        output = None
        if not isinstance(stdin, GeneratorType):
            stdin = (n for n in [stdin,])
        cursor = Register(0, memory)
        while True:
            command = Command(cursor.value)
            if command.opcode not in self.opcodes:
                raise Exception(f"Bad Opcode {command.opcode} ({cursor})")

            instruction = self.opcodes[command.opcode]

            cursor.seek(1)
            # read parameters from memory and act on parameter mode
            parameters = []
            for i in range(instruction.parametercount):
                register = copy(cursor)
                cursor.seek(1)

                if (command.modes[i]) == "0":  # position mode
                    # interpret parameter as memory address to read
                    parameters.append(Register(register.value, memory))
                if (command.modes[i]) == "1":  # immediate mode
                    # interpret parameter as value
                    parameters.append(register)

            # execute opcode
            try:
                ret = instruction.routine(cursor, stdin, parameters, verbose)
                if ret is not None:
                    output = ret
                    if verbose:
                        print("Output:", output)
                    yield ret
            except ProgramHalt:
                break


computer = IntcodeComputer(instructions)
