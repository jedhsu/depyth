"""

    *Aritied Operator, Bindings*

"""
from ._operator import AritiedOperator
from .binary import BinaryOperator
from .nullary import NullaryOperator
from .ternary import TernaryOperator
from .unary import UnaryOperator

__all__ = ["AritiedOperator"]

AritiedOperator.Nullary = NullaryOperator
AritiedOperator.Unary = UnaryOperator
AritiedOperator.Binary = BinaryOperator
AritiedOperator.Ternary = TernaryOperator
