"""

    *Type Parameters,   [Unit Tests]*

"""

from depyt.type.parameter.parameters import Test
from depyt.type.parameter.parameters import TypeParameters


class TestTypeParameters:
    def test_init(self):
        assert isinstance(Test.shape, TypeParameters)
        assert len(Test.shape) == 2

    def test_names(self):
        assert Test.shape.names == (
            "width",
            "height",
        )
