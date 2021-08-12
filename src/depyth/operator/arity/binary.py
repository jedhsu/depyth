"""

    *Binary Operator*

  An operator of arity 2.

"""
from abc import ABCMeta
from dataclasses import dataclass
from typing import Generic
from typing import TypeVar


from ._operator import AritiedOperator
from depyth._type import Type

__all__ = ["BinaryOperator"]


class ParameterType(
    Type,
):
    __metaclass__ = ABCMeta


ParameterType1 = TypeVar("ParameterType1", bound=Type)
ParameterType2 = TypeVar("ParameterType2", bound=Type)

ReturnType = TypeVar("ReturnType", bound=Type)


@dataclass
class BinaryOperator(
    Generic[
        ParameterType1,
        ParameterType2,
        ReturnType,
    ],
    AritiedOperator,
    metaclass=ABCMeta,
):

    _parameter1: ParameterType
    _parameter2: ParameterType

    _return: ReturnType

    def __repr__(self):
        return "{} | {}  ==>  {}".format(
            self._parameter1,
            self._parameter2,
            self._return,
        )
