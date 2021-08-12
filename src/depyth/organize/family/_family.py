"""

    *Type Family*

  Parameterize a type over an index.

"""
from abc import ABCMeta
from typing import Collection

from .._type import Type


class TypeFamily(
    Collection[Type],
):
    __metaclass__ = ABCMeta
