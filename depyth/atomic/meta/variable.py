"""

    *Metavariable*

  Confirm that composite meta-variables are not needed.

"""

from sympy import Symbol

__all__ = ["Metavariable"]


class Metavariable(
    Symbol,
):
    def __init__(
        self,
        symbol: str,
    ):
        super().__new__(
            Metavariable,
            symbol,
        )
