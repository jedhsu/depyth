# """
#     *Integer*
# """
# from __future__ import annotations
# from dataclasses import dataclass
# from .type import ScalarSymbolicType
# from ._symbol import SymbolicExpression
# from ._symbol import Symbol
# __all__ = ["IntegerType"]
# A = Symbol("A")
# B = Symbol("B")
# class IntegerType(
#     ScalarSymbolicType,
#     type,
# ):
#     def __init__(
#         self,
#         expression: SymbolicExpression,
#     ):
#         super(IntegerType, self).__init__(
#             expression,
#         )
# class Integer(
#     metaclass=IntegerType,
# ):
#     integer: int
#     @classmethod
#     def __class_getitem__(
#         cls,
#         symbol: str,
#     ):
#         return cls(symbol)
# @dataclass
# class IntegerOps(
#     Integer,
# ):
#     def __add__(
#         self: Integer[A],
#         b: Integer[B],
#     ) -> Integer[A + B]:
#         return Integer(self.integer - b.integer)
# class TestInteger:
#     a = Integer["A"] + Integer["B"]
