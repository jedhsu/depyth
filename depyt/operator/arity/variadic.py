"""

    *Nullary Operator*

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import TypeVar
from typing import Generic

from wich._type import Type
from wich._form.type import Nothing

from .._operator import Operator

__all__ = ["NullaryOperator"]

T = TypeVar("T")


@dataclass
class NullaryOperator(
    Generic[T],
    Operator[Type, Nothing],
):
    __metaclass__ = ABCMeta
