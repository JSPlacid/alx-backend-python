# python_variable_annotations
![](https://camo.githubusercontent.com/e6e58053238a73487f09c17a7c0bf3e66638aba2cbfba36150f85b61c0c29183/68747470733a2f2f666c6f7269616e2d6461686c69747a2e64652f6d656469612f61727469636c65732f6c657665726167652d7468652d66756c6c2d706f74656e7469616c2d6f662d747970652d68696e74732f7468756d626e61696c2d6d2e77656270)

Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.
For example, in
```
def fn(a, b):
    return a + b
```
The types of a and b are not known at build-time, only when a and b are assigned values at run-time.

Hence, calling
```

def fn(a, b):
    return a + b


fn("a", 1)
```
somewhere in your code will not raise an exception until the code is actually executed and the function is called:
```
>>> fn("a", 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

```
In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:

- Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
- Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.

### Objectives
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy