"""

    *Type Parameters*

"""
from typing import Sequence

from .parameter import TypeParameter

__all__ = ["TypeParameters"]


class TypeParameters(
    dict,
):
    def __init__(
        self,
        dct: dict,
    ):
        super(TypeParameters, self).__init__(
            dct,
        )

    @property
    def names(self) -> Sequence[str]:
        return tuple([param.name for param in self.values()])

    def add(
        self,
        param: TypeParameter,
    ):
        if param.name not in self:
            self[param.name] = param
        return self

    def __repr__(self):
        return " | ".join(["{}".format(v) for v in self.values()])


class Test:
    shape = TypeParameters(
        {
            data[0]: TypeParameter(*data)
            for data in [
                ("width", int, 5),
                ("height", int, 10),
            ]
        }
    )
