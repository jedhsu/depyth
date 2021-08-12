"""

    *Expression Type Parameter*

  Represents parametrization over a space.

"""
from .._symbol import Symbol
from .._symbol import SymbolicExpression
from ._parameter import TypeParameter

__all__ = ["ExpressionTypeParameter"]


class ExpressionTypeParameter(
    SymbolicExpression,
    TypeParameter,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(ExpressionTypeParameter, self).__init__(
            *args,
            **kwargs,
        )


class Test:
    expression = ExpressionTypeParameter(Symbol("A") + Symbol("B"))
    # symbol = ExpressionTypeParameter(Symbol("A"))
