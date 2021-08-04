from ..unary import Test
from ..unary import Integer

from ..unary import UnaryOperator


class TestUnaryOperator:
    def test_init(self):
        op = Test.ConcreteUnaryOperator(
            Integer(1),
            None,
        )
        assert isinstance(op, UnaryOperator)
        assert op.operand == Integer(1)
        assert op.operator is None

    def test_create(self):
        op = Test.ConcreteUnaryOperator.create(
            Integer(1),
        )
        assert isinstance(op, UnaryOperator)
        assert op.operand == Integer(1)
        assert op.operator is None

    def test_from_ast(self):
        pass

    def test_into_ast(self):
        pass
