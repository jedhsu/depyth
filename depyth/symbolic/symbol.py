"""

    *Symbol*

"""

from abc import ABCMeta

from sympy import Symbol as _Symbol

from ._symbolic import Symbolic

__all__ = ["Symbol"]


class Symbol(
    _Symbol,
    Symbolic,
):
    __metaclass__ = ABCMeta

    def __init__(
        self,
        symbol: str,
    ):
        super(Symbol, self).__new__(
            _Symbol,
            symbol,
        )
