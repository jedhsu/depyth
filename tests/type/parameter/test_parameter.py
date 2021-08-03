"""

    *Type Parameter,   [Unit Tests]*

"""

from depyt.type.parameter.parameter import Test
from depyt.type.parameter.parameter import TypeParameter


class TestTypeParameter:
    def test_init(self):
        assert isinstance(Test.int5, TypeParameter)
        assert Test.int5.name == "value"
        assert Test.int5.type == int
        assert Test.int5.value == 5
