"""

    *Ternary Operator*

  An operator of arity 3.

"""
from abc import ABCMeta
from dataclasses import dataclass
from typing import ClassVar
from typing import Generic
from typing import TypeVar

from wich._type import Type

from ._operator import AritiedOperator

__all__ = ["TernaryOperator"]

ParameterType1 = TypeVar("ParameterType1", bound=Type)
ParameterType2 = TypeVar("ParameterType2", bound=Type)
ParameterType3 = TypeVar("ParameterType3", bound=Type)

ReturnType = TypeVar("ReturnType", bound=Type)
NothingType = TypeVar("NothingType", bound=Nothing)


@dataclass
class TernaryOperator(
    Generic[
        ParameterType1,
        ParameterType2,
        ParameterType3,
        ReturnType,
    ],
    AritiedOperator,
    metaclass=ABCMeta,
):

    _parameter1: ParameterType1
    _parameter2: ParameterType2
    _parameter3: ParameterType3

    _return: ReturnType

    def __repr__(self):
        return "{} | {} | {}  ==>  {}".format(
            self._parameter1,
            self._parameter2,
            self._parameter3,
            self._return,
        )
