from abc import ABC, abstractmethod
from typing import List, Optional

from intcode.exceptions import ProgramHalt
from intcode.register import Register


class BaseOpcode(ABC):
    @classmethod
    @abstractmethod
    def code(cls) -> str:
        ...

    @classmethod
    @abstractmethod
    def parametercount(cls):
        ...

    @classmethod
    @abstractmethod
    def __call__(
        cls, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        ...


class Halt(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "99"

    @classmethod
    def parametercount(cls) -> int:
        return 0

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        raise ProgramHalt()


class Add(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "01"

    @classmethod
    def parametercount(cls) -> int:
        return 3

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        parameters[2].value = parameters[0].value + parameters[1].value
        return None  # no output


class Multipy(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "02"

    @classmethod
    def parametercount(cls) -> int:
        return 3

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        parameters[2].value = parameters[0].value * parameters[1].value
        return None  # no output


class Input(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "03"

    @classmethod
    def parametercount(cls) -> int:
        return 1

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        parameters[0].value = input
        return None  # no output


class Output(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "04"

    @classmethod
    def parametercount(cls) -> int:
        return 1

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        return parameters[0].value


class JumpIfTrue(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "05"

    @classmethod
    def parametercount(cls) -> int:
        return 2

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        if parameters[0].value != 0:
            cursor.seek(parameters[1].value, True)  # seek absolute
        return None  # no output


class JumpIfFalse(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "06"

    @classmethod
    def parametercount(cls) -> int:
        return 2

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        if parameters[0].value == 0:
            cursor.seek(parameters[1].value, True)  # seek absolute
        return None  # no output


class LessThan(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "07"

    @classmethod
    def parametercount(cls) -> int:
        return 3

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        parameters[2].value = int(parameters[0].value < parameters[1].value)
        return None  # no output


class Equals(BaseOpcode):
    @classmethod
    def code(cls) -> str:
        return "08"

    @classmethod
    def parametercount(cls) -> int:
        return 3

    @classmethod
    def __call__(
        self, cursor: Register, input: int, parameters: List[Register]
    ) -> Optional[int]:
        parameters[2].value = int(parameters[0].value == parameters[1].value)
        return None  # no output
