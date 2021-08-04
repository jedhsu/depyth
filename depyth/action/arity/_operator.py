"""

    *Aritied Action*

  Action type partitioned by arity.

"""

from abc import ABCMeta

from typing import TypeVar
from typing import Generic

from .._action import Action

__all__ = ["AritiedAction"]


class AritiedAction(
    Action,
):
    __metaclass__ = ABCMeta

    Nullary = TypeVar("Nullary")
    Unary = TypeVar("Unary")
    Binary = TypeVar("Binary")
    Ternary = TypeVar("Ternary")
    Variadic = TypeVar("Variadic")
