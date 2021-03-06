"""

    *Abstract*

  An abstract
  * parameterizes a type.
  * instantiates a value.


"""
from __future__ import annotations

from abc import ABCMeta
from dataclasses import dataclass
from typing import ClassVar

from .parameter import TypeParameters

__all__ = ["Abstract"]


@dataclass
class Abstract(
    type,
    metaclass=ABCMeta,
):

    parameters: ClassVar[TypeParameters] = TypeParameters({})

    @classmethod
    def __prepare__(
        meta,
        name,
        bases,
    ):
        return TypeParameters({})

    def __new__(
        meta,
        name,
        bases,
        params,
    ):
        cls = super(Metatype, meta).__new__(
            meta,
            name,
            bases,
            params,
        )
        cls.parameters = params
        return cls

    def __add__(
        self,
    ):
        pass
