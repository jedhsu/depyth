"""

    *Type Parameters*

"""

from bidict import bidict

__all__ = ["TypeParameters"]


class TypeParameters(
    bidict,
):
    def __init__(self):
        self.parameters: list[str] = []

    def __setitem__(
        self,
        key,
        value,
    ):
        if key not in self:
            self.parameters.append(key)

        dict.__setitem__(self, key, value)
