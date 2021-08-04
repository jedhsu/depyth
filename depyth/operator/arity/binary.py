"""

    *Binary Operator*

  An operator of arity 2.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import Generic
from typing import TypeVar
from typing import ClassVar

from wich._type import Type
from wich._form.type import Nothing

from ...arity import BinaryAction
from ._operator import AritiedOperator

__all__ = ["BinaryOperator"]

ParameterType1 = TypeVar("ParameterType1", bound=Type)
ParameterType2 = TypeVar("ParameterType2", bound=Type)
ParameterType3 = TypeVar("ParameterType3", bound=Type)

ReturnType = TypeVar("ReturnType", bound=Type)


@dataclass
class BinaryOperator(
    BinaryAction[
        ParameterType1,
        ParameterType2,
        ReturnType,
        Nothing,
    ],
    AritiedOperator,
):
    __metaclass__ = ABCMeta

    _effect = ClassVar[Nothing]

    _parameter1: ParameterType1
    _parameter2: ParameterType2

    _return: ReturnType

    def __repr__(self):
        return "{} | {}  ==>  {}".format(
            self._parameter1,
            self._parameter2,
            self._return,
        )
