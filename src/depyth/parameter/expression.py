"""

    *Expression Type Parameter*

  Represents parametrization over a space.

"""

from ._parameter import TypeParameter

from .._symbol import SymbolicExpression
from .._symbol import Symbol

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
