"""

    *Nullary Operator*

  An operator of arity 0.

"""
from abc import ABCMeta
from dataclasses import dataclass
from typing import Generic
from typing import TypeVar

from ._operator import AritiedOperator

__all__ = ["NullaryOperator"]

ReturnType = TypeVar("ReturnType")


@dataclass
class NullaryOperator(
    Generic[
        ReturnType,
    ],
    AritiedOperator,
    metaclass=ABCMeta,
):
    _return: ReturnType

    def __repr__(self):
        return "()  ==>  {}".format(
            self._return,
        )
