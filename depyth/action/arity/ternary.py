"""

    *Ternary Action*

  Actions of arity 3.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import Generic
from typing import TypeVar

from wich._type import Type
from wich._effect import Effect

from ._operator import AritiedAction

__all__ = ["TernaryAction"]

TypeParameter1 = TypeVar("TypeParameter1", bound=Type)
TypeParameter2 = TypeVar("TypeParameter2", bound=Type)
TypeParameter3 = TypeVar("TypeParameter3", bound=Type)

ReturnType = TypeVar("ReturnType", bound=Type)
Effect = TypeVar("Effect", bound=Effect)


@dataclass
class TernaryAction(
    Generic[
        TypeParameter1,
        TypeParameter2,
        TypeParameter3,
        ReturnType,
        Effect,
    ],
    AritiedAction,
):
    __metaclass__ = ABCMeta
