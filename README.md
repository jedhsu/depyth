#### Features
* Dependent type system.
  - Types are first-class.
  - The parameters of a type (the types of it's instantiated attributes) are represented as symbolic expressions. This can build up to extended static checking, albeit with a heavy annotation load.

* Prototyping of effect type via design by contract.


**Making type a variable allows type to best represent its meaning, which is a collection / shape, rather than a point-wise scalar.**

Ultimately, build up to extended static checking as such:

```python

class Hstack:
    Tensor[D][m1, n] + Tensor[D][m2, n] = Tensor[D]
    
```

Influenced by System F, Idris.

Early work in progress.
