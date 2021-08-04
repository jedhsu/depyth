"""

    *Contract*

  A contract is a generalization of a type check.

  In practice, vary the strictness on judgments.

  This is relevant to RL!

"""


from wich._context import Judgment

from dataclasses import dataclass

__all__ = ["Contract"]


@dataclass
class Contract:
    presumptions: set[Judgment]
    conclusions: set[Judgment]
