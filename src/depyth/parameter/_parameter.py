"""

    *Type Parameter*

"""
from abc import ABCMeta
from abc import abstractmethod
from typing import Callable
from typing import ClassVar

__all__ = ["TypeParameter"]


class TypeParameter:
    __metaclass__ = ABCMeta

    def __add__(self):
        raise NotImplementedError

    create = ClassVar[Callable]
