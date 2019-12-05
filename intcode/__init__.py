from typing import List
from copy import copy

from intcode.exceptions import ProgramHalt
from intcode.opcodes import *
from intcode.register import Register


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
            assert opcode not in self.opcodes
            self.opcodes[opcode] = cls()

    def Run(self, memory: List[int], input=None):
        output = None
        cursor = Register(0, memory)
        while True:
            command = Command(cursor.value)
            if command.code not in self.opcodes:
                raise Exception(f"Bad Opcode {command.code} ({cursor})")

            opcode = self.opcodes[command.code]

            cursor.seek(1)
            # read parameters from memory and act on parameter mode
            parameters = []
            for i in range(opcode.parametercount()):
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
                ret = opcode(cursor, input, parameters)
                if ret is not None:
                    output = ret
                    print(output)
            except ProgramHalt:
                break

        return output


intcodemachine = IntcodeMachine(
    [Halt, Add, Multipy, Input, Output, JumpIfTrue, JumpIfFalse, LessThan, Equals]
)
