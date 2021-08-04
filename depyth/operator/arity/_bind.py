"""

    *Aritied Operator, Bindings*

"""

from ._operator import AritiedOperator

from .nullary import NullaryOperator
from .unary import UnaryOperator
from .binary import BinaryOperator
from .ternary import TernaryOperator

__all__ = ["AritiedOperator"]

AritiedOperator.Nullary = NullaryOperator
AritiedOperator.Unary = UnaryOperator
AritiedOperator.Binary = BinaryOperator
AritiedOperator.Ternary = TernaryOperator
