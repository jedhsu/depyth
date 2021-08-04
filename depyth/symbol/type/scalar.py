"""

    *Scalar Symbolic Type*

"""

from __future__ import annotations
from abc import ABCMeta
from dataclasses import dataclass

from typing import Union
from typing import TypeVar
from typing import Generic

from ..parameter import TypeParameter

from sympy import Symbol
from sympy import Expr

__all__ = ["ScalarSymbolicType"]


A = Symbol("A")
B = Symbol("B")


@dataclass
class ScalarSymbolicType(
    type,
):
    __metaclass__ = ABCMeta

    parameter: TypeParameter

    def __repr__(self):
        return "{}[{}]".format(
            self.__class__.__name__,
            self,
        )

    def __eq__(self):
        """
        [TODO] Equality up to alpha equivalence.

        """
        return self.parameter == self.parameter


T = TypeVar("T", bound=ScalarSymbolicType)


class ScalarSymbolicTypeOps(
    Generic[T],
    ScalarSymbolicType,
):
    @classmethod
    def add(
        cls,
        t1: T,
        t2: T,
    ) -> T:
        return cls(
            t1.parameter + t2.parameter,
        )

    def __sub__(
        self,
        other: ScalarSymbolicType,
    ) -> IntegerType:
        return IntegerType(self.parameter - other.parameter)


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
