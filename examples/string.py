from __future__ import annotations
from ._bind import AtomicType

from sympy import Symbol

A = Symbol("A")
B = Symbol("B")


class ConcreteAtomicTestString(
    str,
    AtomicType,
):
    def add(
        self: ConcreteAtomicTestString[A],
        other: ConcreteAtomicTestString[B],
    ) -> ConcreteAtomicTestString[A + B]:
        return ConcreteAtomicTestString(
            self.value + other.value,
        )
