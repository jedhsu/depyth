"""

    *Aritied Operator*

  Operator type partitioned by arity.

"""

from abc import ABCMeta
from typing import TypeVar

from .._operator import Operator

__all__ = ["AritiedOperator"]


class AritiedOperator(
    Operator,
):
    __metaclass__ = ABCMeta

    Nullary = TypeVar("Nullary")
    Unary = TypeVar("Unary")
    Binary = TypeVar("Binary")
    Ternary = TypeVar("Ternary")
