"""

    *Atomic Type*

  An atomic type.

"""
from typing import Any

from .._type import Type
from .abstract import Abstract

__all__ = ["AtomicType"]


class AtomicType(
    Type,
    metaclass=Abstract,
):
    value: Any

    def parametrize(self):
        return AtomicTypeVariable


# class Test:
#     TypeA = BasicType[("value", A)]
#     # TypeAPlusB = Type[A + B]
#     # TypeABC = Type[A][B][C]
