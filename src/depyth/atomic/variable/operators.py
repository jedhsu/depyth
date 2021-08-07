"""

  Closed operators for atomic type variables.

"""

from ._variable import AtomicTypeVariable


def add(
    left: AtomicTypeVariable,
    right: AtomicTypeVariable,
):
    return AtomicTypeVariable(left + right)
