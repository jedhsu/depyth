from ._operator import AritiedOperator

from .nullary import NullaryOperator
from .unary import UnaryOperator
from .binary import BinaryOperator
from .ternary import TernaryOperator

__all__ = [
    "AritiedOperator",
    "NullaryOperator",
    "UnaryOperator",
    "BinaryOperator",
    "TernaryOperator",
]
