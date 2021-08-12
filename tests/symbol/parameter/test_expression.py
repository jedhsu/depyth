"""

    *Expression Type Parameter,   [Bindings]*

"""
from depyt.symbol.parameter.expression import ExpressionTypeParameter
from depyt.symbol.parameter.expression import SymbolicExpression
from depyt.symbol.parameter.expression import Test
from sympy import Expr


class TestExpressionTypeParameter:
    def test_init(self):
        assert isinstance(Test.expression, ExpressionTypeParameter)
        assert isinstance(Test.expression, SymbolicExpression)
        assert isinstance(Test.expression, Expr)
