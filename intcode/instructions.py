from abc import ABC, abstractmethod
from typing import List, Optional

from intcode.exceptions import ProgramHalt
from intcode.register import Register


def Instruction(name: str, opcode: str, parameters: int, routine):
    return type(
        name,
        (object,),
        {"opcode": opcode, "parametercount": parameters, "routine": routine},
    )


def Halt(cursor: Register, input: int, parameters: List[Register]):
    raise ProgramHalt()


def Add(cursor: Register, input: int, parameters: List[Register]):
    parameters[2].value = parameters[0].value + parameters[1].value
    return None  # no output


def Multipy(cursor: Register, input: int, parameters: List[Register]):
    parameters[2].value = parameters[0].value * parameters[1].value
    return None  # no output


def Input(cursor: Register, input: int, parameters: List[Register]):
    parameters[0].value = input
    return None  # no output


def Output(cursor: Register, input: int, parameters: List[Register]):
    return parameters[0].value


def JumpIfTrue(cursor: Register, input: int, parameters: List[Register]):
    if parameters[0].value != 0:
        cursor.seek(parameters[1].value, True)  # seek absolute
    return None  # no output


def JumpIfFalse(cursor: Register, input: int, parameters: List[Register]):
    if parameters[0].value == 0:
        cursor.seek(parameters[1].value, True)  # seek absolute
    return None  # no output


def LessThan(cursor: Register, input: int, parameters: List[Register]):
    parameters[2].value = int(parameters[0].value < parameters[1].value)
    return None  # no output


def Equals(cursor: Register, input: int, parameters: List[Register]):
    parameters[2].value = int(parameters[0].value == parameters[1].value)
    return None  # no output


instructions = (
    Instruction("Halt", "99", 0, Halt),
    Instruction("Add", "01", 3, Add),
    Instruction("Multipy", "02", 3, Multipy),
    Instruction("Input", "03", 1, Input),
    Instruction("Output", "04", 1, Output),
    Instruction("JumpIfTrue", "05", 2, JumpIfTrue),
    Instruction("JumpIfFalse", "06", 2, JumpIfFalse),
    Instruction("LessThan", "07", 3, LessThan),
    Instruction("Equals", "08", 3, Equals),
)
