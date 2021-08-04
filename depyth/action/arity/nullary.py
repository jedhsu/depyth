"""

    *Nullary Action*

  Actions of arity 0.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import Generic
from typing import TypeVar

from wich._type import Type
from wich._effect import Effect

from ._operator import AritiedAction

__all__ = ["NullaryAction"]

ReturnType = TypeVar("ReturnType", bound=Type)
Effect = TypeVar("Effect", bound=Effect)


@dataclass
class NullaryAction(
    Generic[
        ReturnType,
        Effect,
    ],
    AritiedAction,
):
    __metaclass__ = ABCMeta

    _return: ReturnType
    _effect: Effect

    def __repr__(self):
        return "()  ==>  {} .. {}".format(
            self._return,
            self._effect,
        )
