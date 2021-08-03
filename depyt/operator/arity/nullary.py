"""

    *Nullary Operator*

  An operator of arity 0.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import Generic
from typing import TypeVar
from typing import ClassVar

from wich._type import Type
from wich._form.type import Nothing

from wich._action import NullaryAction
from ._operator import AritiedOperator

__all__ = ["NullaryOperator"]

ReturnType = TypeVar("ReturnType", bound=Type)
NothingType = TypeVar("NothingType", bound=Nothing)


@dataclass
class NullaryOperator(
    NullaryAction[
        ReturnType,
        Nothing,
    ],
    AritiedOperator,
):
    __metaclass__ = ABCMeta

    _effect = ClassVar[Nothing]

    _return: ReturnType

    def __repr__(self):
        return "()  ==>  {}".format(
            self._return,
        )
