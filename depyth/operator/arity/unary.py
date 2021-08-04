"""

    *Unary Operator*

  An operator of arity 1.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import TypeVar
from typing import ClassVar

from wich._type import Type
from wich._form.type import Nothing

from wich._action import UnaryAction
from ._operator import AritiedOperator

__all__ = ["UnaryOperator"]

ParameterType1 = TypeVar("ParameterType1", bound=Type)

ReturnType = TypeVar("ReturnType", bound=Type)
NothingType = TypeVar("NothingType", bound=Nothing)


@dataclass
class UnaryOperator(
    UnaryAction[
        ParameterType1,
        ReturnType,
        Nothing,
    ],
    AritiedOperator,
):
    __metaclass__ = ABCMeta
    _effect = ClassVar[Nothing]

    _parameter1: ParameterType1
    _return: ReturnType

    def __repr__(self):
        return "{}  ==>  {}".format(
            self._parameter1,
            self._return,
        )
