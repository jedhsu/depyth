"""

    *Variable Type Parameter,   [Bindings]*

"""

from depyt.symbol.parameter.variable import Test

from depyt.symbol.parameter.variable import Symbol
from depyt.symbol.parameter.variable import VariableTypeParameter


class TestVariableTypeParameter:
    def test_init(self):
        assert isinstance(Test.symbol, VariableTypeParameter)
        assert isinstance(Test.symbol, Symbol)
        assert repr(Test.symbol) == "A"
