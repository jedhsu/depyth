"""

    *Fraction*

  Example.

"""
from dataclasses import dataclass

from depyth.symbol import A
from depyth.symbol import Integer


@dataclass
class Fraction(
    Type,
):
    numerator: Integer
    denominator: Integer


class FractionOps(
    Fraction,
):
    def __add__(
        self: Fraction[
            Integer[A],
            Integer[B],
        ],
        other: Fraction[
            Integer[C],
            Integer[D],
        ],
    ) -> Fraction[Integer[A * D], Integer[B * C],]:
        return Fraction(
            (self.numerator * other.denominator),
            (other.numerator * self.denominator),
        )
