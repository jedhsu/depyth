"""

    *Atomic Type Add*

"""

from sympy import Symbol

from depyth.operator.arity import BinaryOperator

from .._bind import AtomicType

A = Symbol("A")
B = Symbol("B")

__all__ = ["AtomicTypeVariableAdd"]


class AtomicTypeAdd(
    BinaryOperator[
        AtomicType[A],
        AtomicType[B],
    ],
    AtomicType[A + B],
):
    @classmethod
    def evaluate(cls):
        cls.parameter1

    # @classmethod
    # def add(
    #     cls,
    #     t1: Type[A],
    #     t2: T,
    # ) -> T:
    #     return cls(
    #         t1.parameter + t2.parameter,
    #     )


# # class ScalarSymbolicTypeOps(
# #     Generic[T],
# #     ScalarSymbolicType,
# # ):

# #     def __sub__(
# #         self,
# #         other: ScalarSymbolicType,
# #     ) -> IntegerType:
# #         return IntegerType(self.parameter - other.parameter)
