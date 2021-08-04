"""

    *Binary Action*

  Actions of arity 2.

"""

from abc import ABCMeta
from dataclasses import dataclass

from typing import Generic
from typing import TypeVar

from wich._type import Type
from wich._effect import Effect

from ._operator import AritiedAction

__all__ = ["BinaryAction"]

TypeParameter1 = TypeVar("TypeParameter1", bound=Type)
TypeParameter2 = TypeVar("TypeParameter2", bound=Type)

ReturnType = TypeVar("ReturnType", bound=Type)
Effect = TypeVar("Effect", bound=Effect)


@dataclass
class BinaryAction(
    Generic[
        TypeParameter1,
        TypeParameter2,
        ReturnType,
        Effect,
    ],
    AritiedAction,
):
    __metaclass__ = ABCMeta
