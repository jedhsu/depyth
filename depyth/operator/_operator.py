"""

    *Operator*

"""

from abc import ABCMeta
from abc import abstractmethod

__all__ = ["Operator"]


class Operator:
    __metaclass__ = ABCMeta

    @classmethod
    def __class_getitem__(cls):
        pass

    @classmethod
    def expression(cls):
        """
        Expression is comprised of metavariables, thus Type is a meta variable.

        """
        pass

    @classmethod
    def evaluate_variables(cls):
        raise NotImplementedError

    @abstractmethod
    def evaluate_values(self):
        raise NotImplementedError
