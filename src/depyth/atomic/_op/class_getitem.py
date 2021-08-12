"""

    *Class Get-Item*

"""
from sympy import Symbol

from .._type import Type
from ..variable import TypeVariable

__all__ = ["ClassGetItem"]


class ClassGetItem(
    Type,
):
    @classmethod
    def __class_getitem__(
        cls,
        symbol: Symbol,
    ) -> TypeVariable:
        return TypeVariable(symbol)
