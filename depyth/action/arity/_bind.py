"""

    *Aritied Action, Bindings*

"""

from ._operator import AritiedAction

from .nullary import NullaryAction
from .unary import UnaryAction
from .binary import BinaryAction
from .ternary import TernaryAction

__all__ = ["AritiedAction"]

AritiedAction.Nullary = NullaryAction
AritiedAction.Unary = UnaryAction
AritiedAction.Binary = BinaryAction
AritiedAction.Ternary = TernaryAction
