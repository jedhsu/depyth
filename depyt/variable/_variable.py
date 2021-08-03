from __future__ import annotations


class Bark:
    pass


@algorithm
class Variable(Operator):
    pass


class Algorithm(
    Operator[A, B, C],
):
    pass


@form
class Chain:
    pass


@interface
class Function(
    Operator,
):
    pass


@algorithm
class Function(
    Operator,
):
    pass


@values
class Monad(
    Values,
):
    pass


"""
Maps into context.
"""


class Map(
    Operator[
        Functor[A, B],
        A,
        B.Functor[A],
    ]
):
    pass


class Apply(
    Operator[
        Applicative[A],
        Applicative[
            Fn[
                A,
                B,
            ],
        ],
        Applicative[B],
    ]
):
    pass


class Bind(
    Operator[
        Monad[A],
        Fn[
            A,
            Monad[B],
        ],
        Monad[B],
    ],
):
    pass
