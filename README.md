## depyth

#### Motivation - Types and Classes

I feel like confusion stems from confounding types and classes, when they are in fact concepts at different layers of abstraction. Classes exist as a syntax construct of the language.

Consider that a Python class is an expansion form, while effectively assigning a hash value to a set of values. This is why it works until composability of the type as a space.

#### Modeling Structure

Values       *are represented by*        Values     *which compose into*

Values expand and reduce under closed operations.
Expressions do not.
Variables thus parametrize over the space of a type.

Thus there are value expressions & variable expressions - we must distinguish.
- when specifying the expression, you want to work with structure - so you need abstract expression.

Abstract types (or abstracts) *parametrize* into types, and *instantiate* into values.


Parameters      Expressions         Variables
Types have metavariables.


#### Features
* Dependent type system.
  - Types are first-class.
  - The parameters of a type (the types of it's instantiated attributes) are represented as symbolic expressions. This can build up to extended static checking, albeit with a heavy annotation load.

* Prototyping of effect type via design by contract.


**Representing a type using a variable best captures its meaning, which is a collection / shape, as opposed to a point-wise element.**

Dependent types enable static assertion on type parameters, (albeit no guarantees on soundness):

```python
def horizontal_stack(m1: Matrix[D][m1, n], m2: Matrix[D][m2, n]) -> Matrix[D][m1 + m2, n]:
    ...
    
```

Influenced by System F, Idris.

Early work in progress.
