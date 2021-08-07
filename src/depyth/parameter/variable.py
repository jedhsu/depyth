"""

    *Variable Type Parameter*

  Represents parametrization over a space.

  Polymorphic type.

"""

from sympy import Symbol

from ._parameter import TypeParameter

__all__ = ["VariableTypeParameter"]


class VariableTypeParameter(
    Symbol,
    TypeParameter,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(VariableTypeParameter, self).__init__(
            *args,
            **kwargs,
        )


class Test:
    symbol = VariableTypeParameter("A")
    # symbol = VariableTypeParameter(Symbol("A"))
