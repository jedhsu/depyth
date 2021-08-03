"""

    *Type Parameter*

  Only scalar types for now.

"""

from dataclasses import dataclass

from typing import Any as Uni

__all__ = ["TypeParameter"]


@dataclass
class TypeParameter:
    name: str
    type: type
    value: Uni

    @classmethod
    def from_tuple(
        cls,
        param: tuple,
    ):
        return cls(
            param[0],
            param.__class__,
            param[1],
        )

    def __repr__(self) -> str:
        return "{}: {}".format(self.name, self.value)


class Test:
    int5 = TypeParameter(
        "value",
        int,
        5,
    )
