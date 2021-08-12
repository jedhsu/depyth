"""

    *Type Sequence*

  A sequence of types parametrized by an index.

  Can be countably infinite.

"""
from abc import ABCMeta
from abc import abstractmethod

from ._family import TypeFamily

__all__ = ["TypeSequence"]


class TypeSequence(
    TypeFamily,
):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __getitem__(
        self,
        index: int,
    ):
        pass
