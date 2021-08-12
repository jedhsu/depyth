## depyth

`depyth` extends Python with components of a dependent type system.

### Goals

We will define a language model on top of the Python language model such that **abstract forms**,
which represent meta-syntax, *parametrize* into **type forms**, and *instantiate* into **value forms**.

We represent types by symbolic expressions, implemented via Sympy. This creates an internal representation
as to what constitutes a value: an object that has the form of a value in Python that does not
implement the symbolic expression protocol.

Thus, type-checking will constitute of evaluation of these variable expressions, and checking that the result is
well-formed.

### Type Composability

We want to implement the semantics of the following feature:

```python
# returns the unique type representing the space of all tensors
T = Tensor

# returns the unique type representing the space of all 2-D tensors (matrices)
T = Tensor[A, B]

# returns True, from alpha equivalence
Tensor[A, B] == Tensor[C, D]

```

Assume tensor is parametrized by its datatype and shape. Note that we will want:

```python
# returns False
Tensor == Tensor[A, B]

# returns True
Tensor[C, D] == Tensor[C, D][A]

```

This means we need some internal mechanism to check
the type variables remaining that are undeclared.

On syntax, I am trying something like the above for now, and if this creates problems,

I will switch to something more explicit, such as 

```python
# returns abstract
Tensor.form

# returns type
Tensor.parametrize().form

# returns value
Tensor.instantiate(...).form
```


### Type Analysis

We want to be able to implement the following, and have the type be verifiable with static analysis.

```python
class Fraction:
    def __add__(
        self: Fraction[
            Integer[A],
            Integer[B],
        ],
        other: Fraction[
            Integer[C],
            Integer[D],
        ],
    ) -> Fraction[
        Integer[A * D],
        Integer[B * C],
    ]:
        return Fraction(
            (self.numerator * other.denominator),
            (other.numerator * self.denominator),
        )
```

### Remarks

Mypy defines types as sets of values and operators, and defines the subtype relation. Focusing on the *sets of values* part, the idea of a set is already [ambiguous](https://plato.stanford.edu/entries/logic-intuitionistic/).

Homotopy theory gives a definition that creates less problems for the notion of equivalence. It gives a weaker statement on types,
defining their values as a space. This frees our reasoning to be point-free, vs. pointful.

Each symbolic type imbues it with the internal representation of a variable, which probably [does not exist in Python on its own](https://existentialtype.wordpress.com/2013/07/22/there-is-such-a-thing-as-a-declarative-language/).

For a primitive type like int, we want the type space to be a zero-dimensional point that is homotopic to the value space. The type is identified by the representation of the point,
and the value is the arrow that evaluates to a point in the value space.

In this sense, types are nothing more than a set of arrows between spaces, and sets of arrows combining arrow.

With this intuition, dependent type theory - the parametrization of type variables by other types - feels less confusing. It is simply taking these geometric representations, and stretching them to a subshape of their final shape earlier in the evaluation chain.

The reasoning to [only instantiate from abstract types](.https://docs.julialang.org/en/v1/manual/types/) is that it creates an unambiguous instantiation chain of point maps until the final mapping, instantiation.

