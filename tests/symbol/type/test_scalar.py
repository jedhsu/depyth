"""

    *Scalar Symbolic Type*

"""

from depyt.symbol.type.scalar import TestConstant
from depyt.symbol.type.scalar import TestVariable
from depyt.symbol.type.scalar import TestExpression

from depyt.symbol.type.scalar import A
from depyt.symbol.type.scalar import B

from depyt.symbol.type.scalar import ScalarSymbolicType
from depyt.symbol.type.scalar import TypeParameter
from depyt.symbol.type.scalar import IntegerExample


class TestScalarConstant:
    def test_init(self):
        assert isinstance(TestConstant.ty, ScalarSymbolicType)
        assert TestConstant.ty.parameter == TypeParameter.create(5)

    def test_repr(self):
        assert repr(TestConstant.ty) == "IntegerExample[5]"

    def test_eq(self):
        pass


class TestScalarVariable:
    def test_init(self):
        assert isinstance(TestVariable.ty, ScalarSymbolicType)
        assert TestVariable.ty.parameter == TypeParameter.create(A)

    def test_repr(self):
        assert repr(TestVariable.ty) == "IntegerExample[A]"


class TestScalarExpression:
    def test_init(self):
        assert isinstance(TestExpression.ty, ScalarSymbolicType)
        assert TestExpression.ty.parameter == TypeParameter.create(A + B)

    def test_repr(self):
        assert repr(TestExpression.ty) == "IntegerExample[A + B]"
