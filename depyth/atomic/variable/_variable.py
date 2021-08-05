"""

    *Atomic Type Variable*

  A generic atomic type variable, represented by a symbol.

"""

from __future__ import annotations
from dataclasses import dataclass

from abc import ABCMeta
from abc import abstractmethod


from sympy import Symbol

from .._type import AtomicType

__all__ = ["AtomicTypeVariable"]


A = Symbol("A")
B = Symbol("B")


@dataclass
class AtomicTypeVariable(
    Symbol,
):
    __metaclass__ = ABCMeta

    type: AtomicType

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(AtomicTypeVariable, self).__init__(
            *args,
            **kwargs,
        )

    def __repr__(self):
        return "{}[{}]".format(
            self.__class__.__name__,
            self,
        )

    @abstractmethod
    def __add__(self, var: AtomicTypeVariable) -> AtomicTypeVariable:
        return AtomicTypeVariable(self + var)


#     def __eq__(self):
#         """
#         [TODO] Equality up to alpha equivalence.

#         """
#         return self.parameter == self.parameter


# T = TypeVar("T", bound=ScalarSymbolicType)


# class Scalar(
#     metaclass=ScalarSymbolicType,
# ):
#     @classmethod
#     def __class_getitem__(
#         cls,
#         param: Union[int, Symbol, Expr],
#     ):
#         return cls(TypeParameter.create(param))


# class IntegerExample(
#     int,
#     Scalar,
# ):
#     def __init__(
#         self,
#         val: int,
#     ):
#         super(IntegerExample, self).__new__(
#             int,
#             val,
#         )


# class TestConstant:
#     ty = IntegerExample[5]


# class TestVariable:
#     ty = IntegerExample[A]


# class TestExpression:
#     ty = IntegerExample[A + B]
