"""

    *Action*

  Returns a type and produces an effect.

"""

from abc import ABCMeta

__all__ = ["Action"]


class Action:
    __metaclass__ = ABCMeta

    @classmethod
    def __class_getitem__(cls, item):
        return item
