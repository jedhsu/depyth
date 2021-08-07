"""

    *Typing Judgment*

"""

from depyth.operator import Operator


class TypingJudgment(
    bool,
):
    def __init__(
        self,
        value: bool,
    ):
        super().__new__(
            bool,
            value,
        )


def judge(cls: type[Operator]):
    result = cls.evaluate()
