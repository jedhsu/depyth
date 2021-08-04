"""

    *Unary Action*

  Actions of arity 1.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import Generic
from typing import TypeVar

from wich._type import Type
from wich._effect import EffectType

from ._operator import AritiedAction

__all__ = ["UnaryAction"]

Param1Type = TypeVar("Param1Type", bound=Type)
ReturnType = TypeVar("ReturnType", bound=Type)
EffectType = TypeVar("EffectType", bound=EffectType)


@dataclass
class UnaryAction(
    Generic[
        Param1Type,
        ReturnType,
        EffectType,
    ],
    AritiedAction,
):
    __metaclass__ = ABCMeta

    _param1: Param1Type

    _return: ReturnType
    _effect: EffectType

    def __repr__(self):
        return "{}  ==>  {} .. {}".format(
            self._param1,
            self._return,
            self._effect,
        )
