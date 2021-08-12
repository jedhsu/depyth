"""

    *Symbolic Expression*

"""
from abc import ABCMeta

from sympy import Expr

__all__ = ["SymbolicExpression"]


class SymbolicExpression(
    Expr,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(SymbolicExpression, self).__new__(
            Expr,
            *args,
            **kwargs,
        )
