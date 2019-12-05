from abc import ABC, abstractmethod
from typing import List, Optional

from intcode.exceptions import ProgramHalt
from intcode.memory import Memory, Register


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
        cls, memory: Memory, input: int, parameters: List[Register]
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
        self, memory: Memory, input: int, parameters: List[Register]
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
        self, memory: Memory, input: int, parameters: List[Register]
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
        self, memory: Memory, input: int, parameters: List[Register]
    ) -> Optional[int]:
        parameters[2].value = parameters[0].value * parameters[1].value
        return None  # no output
