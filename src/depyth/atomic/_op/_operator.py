"""

    *Atomic Type Operator*

"""
from abc import ABCMeta
from dataclasses import dataclass

from depyth.operator import Operator


@dataclass
class AtomicTypeOperator(
    Operator,
    metaclass=ABCMeta,
):
    pass
