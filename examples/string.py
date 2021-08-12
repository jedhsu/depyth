from __future__ import annotations

from sympy import Symbol

from ._bind import AtomicType

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
