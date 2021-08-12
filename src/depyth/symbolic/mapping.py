"""

    *Symbolic Mapping*

"""
from dataclasses import dataclass

from ._symbolic import Symbolic

__all__ = ["SymbolicMapping"]


@dataclass
class SymbolicMapping(
    dict[str, Symbolic],
    Symbolic,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(SymbolicMapping, self).__init__(
            *args,
            **kwargs,
        )
