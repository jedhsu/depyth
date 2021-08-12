"""

    *Symbolic Expression*

"""
from wich._type import Type

from .._symbol import Symbol
from .parameters import ExpressionParameters

__all__ = ["SymbolicExpressionType"]


class SymbolicExpressionType(
    type,
    Type,
):
    @classmethod
    def __prepare__(
        metacls,
        name,
        bases,
    ):
        return ExpressionParameters()

    def __new__(
        meta,
        name,
        bases,
        clsdct,
    ):
        cls = super(SymbolicExpressionType, meta).__new__(
            meta,
            name,
            bases,
            clsdct,
        )
        cls.parameters = clsdct.parameters
        return cls
