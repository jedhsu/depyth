"""

    *Type Parameter, Bindings*

"""

from ._parameter import TypeParameter

from .constant import ConstantTypeParameter
from .variable import VariableTypeParameter

__all__ = ["TypeParameter"]


def create(param):
    if isinstance(param, str):
        return VariableTypeParameter(param)
    elif isinstance(param, int):
        return ConstantTypeParameter(param)
    else:
        raise TypeError


TypeParameter.create = create
