"""

    *Atomic Type*

  An atomic type.

"""

from typing import Any

from .._type import Type

from .meta import Metatype
from .meta import Metavariable

from sympy import Symbol

__all__ = ["AtomicType"]


class AtomicType(
    Metavariable,
    Type,
):
    __metaclass__ = Metatype

    value: Any

    def parametrize(self):
        return AtomicTypeVariable


# class Test:
#     TypeA = BasicType[("value", A)]
#     # TypeAPlusB = Type[A + B]
#     # TypeABC = Type[A][B][C]
