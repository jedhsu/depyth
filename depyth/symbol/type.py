"""

    *Symbolic Type*

"""

from dataclasses import dataclass
from sympy import Symbol

__all__ = ["SymbolicType"]


@dataclass
class SymbolicType(
    Symbol,
):
    type: type

    def __repr__(self):
        return "{}[{}]".format(self.type, self)
