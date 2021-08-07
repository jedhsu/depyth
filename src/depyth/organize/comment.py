"""

Type comment.

"""

from __future__ import annotations
import ast
from dataclasses import dataclass
from typing import final

from ..base import Token

__all__ = ["TypeComment"]


@final
@dataclass
class TypeComment(Token):

    _node = ast.TypeIgnore  # [TODO] check why so specific?

    lineno: int
    tag: str

    @classmethod
    def from_ast(cls, node: ast.TypeIgnore) -> TypeComment:
        ...
