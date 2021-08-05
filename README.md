#### Features
* Dependent type system.
  - Types are first-class.
  - The parameters of a type (the types of it's instantiated attributes) are represented as symbolic expressions. This can build up to extended static checking, albeit with a heavy annotation load.

* Prototyping of effect type via design by contract.


**Representing a type using a variable best captures its meaning, which is a collection / shape, as opposed to a point-wise element.**

Ultimately, this opens up extended static assertion (albeit no guarantees on soundness):

```python
class Hstack:
    Matrix[D][m1, n] + Matrix[D][m2, n] = Matrix[D][m1 + m2, n]
    
```

Influenced by System F, Idris.

Early work in progress.
