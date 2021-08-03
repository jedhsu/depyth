"""

    *Composite Symbolic Type*

"""

from depyt.symbol.type.composite import TestExpression


class TestCompositeExpression:
    def test_repr(self):
        assert repr(TestExpression.ty) == "ComplexNumber[Real[A], Imaginary[B]]"
