"""

    *op . ary*

  Types by operator arity.

  Forms a partition on Action.

"""


from ._operator import AritiedAction

from .nullary import NullaryAction
from .unary import UnaryAction
from .binary import BinaryAction
from .ternary import TernaryAction

__all__ = [
    "AritiedAction",
    "NullaryAction",
    "UnaryAction",
    "BinaryAction",
    "TernaryAction",
]
