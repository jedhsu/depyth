"""

    *Constant Type Parameter*

  Start with int for now, extend later.

"""

from ._parameter import TypeParameter

__all__ = ["ConstantTypeParameter"]


class ConstantTypeParameter(
    int,
    TypeParameter,
):
    def __init__(
        self,
        value: int,
    ):
        super(ConstantTypeParameter, self).__new__(
            int,
            value,
        )


class Test:
    integer = ConstantTypeParameter(5)
