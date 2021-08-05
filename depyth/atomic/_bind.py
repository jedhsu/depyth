"""

    *Atomic Type, Bindings*

"""

from ._type import AtomicType as _AtomicType
from ._op import ClassGetItem

__all__ = ["AtomicType"]


class AtomicType(
    ClassGetItem,
    _AtomicType,
):
    pass
