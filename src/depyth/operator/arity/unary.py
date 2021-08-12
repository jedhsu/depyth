"""

    *Unary Operator*

  An operator of arity 1.

"""
from abc import ABCMeta
from dataclasses import dataclass
from typing import Generic
from typing import TypeVar

from ._operator import AritiedOperator

__all__ = ["UnaryOperator"]

ParameterType1 = TypeVar("ParameterType1")

ReturnType = TypeVar("ReturnType")


@dataclass
class UnaryOperator(
    Generic[
        ParameterType1,
        ReturnType,
    ],
    AritiedOperator,
    metaclass=ABCMeta,
):

    _parameter1: ParameterType1
    _return: ReturnType

    def __repr__(self):
        return "{}  ==>  {}".format(
            self._parameter1,
            self._return,
        )
