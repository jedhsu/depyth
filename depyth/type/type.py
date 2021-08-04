"""

    *Type*

"""

from __future__ import annotations
from dataclasses import dataclass

from typing import Any


from sympy import Symbol

from .meta import Metatype

__all__ = ["Type"]


A = Symbol("A")
B = Symbol("B")
C = Symbol("C")


class Type:
    __metaclass__ = Metatype

    @classmethod
    def __class_getitem__(
        cls,
        *item: tuple[str, Any],
    ):
        return cls(*item)


@dataclass
class BasicType(
    Type,
):
    value: int = Symbol.next()

    def add(
        self: BasicType[("value", A)],
        other: BasicType[("value", B)],
    ) -> BasicType[("value", A + B)]:
        return BasicType(self.value + other.value)


class Test:
    TypeA = BasicType[("value", A)]
    # TypeAPlusB = Type[A + B]
    # TypeABC = Type[A][B][C]
