"""

    *Type Mapping*

  A mapping of types.

  # [TODO] Can probably group with sequence.

"""
from abc import ABCMeta
from abc import abstractmethod
from typing import Hashable

from .._type import Type
from ._family import TypeFamily

__all__ = ["TypeMapping"]


class TypeMapping(
    TypeFamily,
):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __getitem__(
        self,
        key: Hashable,
    ) -> Type:
        pass
