from abc import ABC, abstractmethod
from typing import List, Optional

from intcode.exceptions import ProgramHalt
from intcode.register import Register
from intcode.state import State


def Instruction(name: str, opcode: str, parameters: int, routine):
    return type(
        name,
        (object,),
        {"opcode": opcode, "parametercount": parameters, "routine": routine},
    )


def Halt(state: State, parameters: List[Register]):
    raise ProgramHalt()


def Add(state: State, parameters: List[Register]):
    parameters[2].value = parameters[0].value + parameters[1].value
    return None  # no output


def Multipy(state: State, parameters: List[Register]):
    parameters[2].value = parameters[0].value * parameters[1].value
    return None  # no output


def Input(state: State, parameters: List[Register]):
    value = next(state.stdin)
    if state.verbose:
        print("Input:", value)
    parameters[0].value = value
    return None  # no output


def Output(state: State, parameters: List[Register]):
    return parameters[0].value


def JumpIfTrue(state: State, parameters: List[Register]):
    if parameters[0].value != 0:
        state.cursor.seek(parameters[1].value, True)  # seek absolute
    return None  # no output


def JumpIfFalse(state: State, parameters: List[Register]):
    if parameters[0].value == 0:
        state.cursor.seek(parameters[1].value, True)  # seek absolute
    return None  # no output


def LessThan(state: State, parameters: List[Register]):
    parameters[2].value = int(parameters[0].value < parameters[1].value)
    return None  # no output


def Equals(state: State, parameters: List[Register]):
    parameters[2].value = int(parameters[0].value == parameters[1].value)
    return None  # no output


def OffsetRelativeBase(state: State, parameters: List[Register]):
    state.relativebase += parameters[0].value
    return None


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
    Instruction("Equals", "09", 1, OffsetRelativeBase),
)
