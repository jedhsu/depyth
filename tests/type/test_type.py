"""

    *Test Type*

"""
from depyt.type.type import A
from depyt.type.type import B
from depyt.type.type import BasicType
from depyt.type.type import Test


class TestType:
    def test_class_getitem(self):
        assert BasicType.__class_getitem__(("value", A)) == BasicType[("value", A)]

    def test_init(self):
        a = BasicType()
        b = BasicType(1)
        assert a == b
        # assert BasicType[("value", B)].parameters is None, BasicType[
        #     ("value", B)
        # ].parameters
