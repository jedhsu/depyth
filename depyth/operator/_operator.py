"""

    *Operator*

"""

from abc import ABCMeta

from .._action import Action

__all__ = ["Operator"]


class Operator(
    Action,
):
    __metaclass__ = ABCMeta

    @classmethod
    def __class_getitem__(cls):
        pass
