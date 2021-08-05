"""

    *Symbolic Sequence*

"""

from dataclasses import dataclass

from ._symbol import Symbol
from ._symbolic import Symbolic

__all__ = ["SymbolicSequence"]


@dataclass
class SymbolicSequence(
    tuple[Symbolic, ...],
    Symbolic,
):
    def __init__(
        self,
        *symbol: Symbol,
    ):
        super(SymbolicSequence, self).__new__(
            tuple,
            [*symbol],
        )
