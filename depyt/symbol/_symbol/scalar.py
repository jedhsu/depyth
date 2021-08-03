"""

    *Symbol*

"""

from abc import ABCMeta

from sympy import Symbol as _Symbol

__all__ = ["Symbol"]


class Symbol(
    _Symbol,
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
