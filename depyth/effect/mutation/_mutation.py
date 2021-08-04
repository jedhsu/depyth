"""

    *Mutation*

  Mutation of an abstraction within the interpreter.

  This is opposed to something like file io.

  *Mutation is an operator on a variable.*

   Possibly key is the idea that effects are operators! and thus functions.

   Call these effectors.

"""

from .._effect import Effect

__all__ = ["Effect"]


class Mutation(
    Effect,
):
    pass
