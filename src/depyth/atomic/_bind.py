"""

    *Atomic Type, Bindings*

"""
from ._op import ClassGetItem
from ._type import AtomicType as _AtomicType

__all__ = ["AtomicType"]


class AtomicType(
    ClassGetItem,
    _AtomicType,
):
    pass
