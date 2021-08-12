"""

    *Type*

"""
from abc import ABCMeta

__all__ = ["Type"]

from ._parameters import TypeParameters


class Type(
    type,
):
    __metaclass__ = ABCMeta

    @classmethod
    def __prepare__(
        metacls,
        name,
        bases,
    ):
        return TypeParameters()

    def __new__(
        meta,
        name,
        bases,
        clsdct,
    ):
        cls = super(Type, meta).__new__(
            meta,
            name,
            bases,
            clsdct,
        )
        cls.parameters = clsdct.parameters
        return cls
