CountMinSketch
==============

This is a minimalistic
`Count-min Sketch <http://en.wikipedia.org/wiki/Count%E2%80%93min_sketch>`_
for Python, featuring some cool things like:
 - Being able to count anything that is hash-able by python (numbers, strings, tuples, inmutables, duck-typeds, etc.).
 - Tests
 - No dependencies
 - No foreign languages, just 100% python.

This software was written by Rafael Carrascosa, you can contact me at
rafacarrascosa on gmail.


Usage
=====

.. code-block:: python

    from countminsketch import CountMinSketch
    sketch = CountMinSketch(1000, 10)  # table size=1000, hash functions=10
    sketch.add("oh yeah")
    sketch.add(tuple())
    sketch.add(1, value=123)
    print sketch["oh yeah"]       # prints 1
    print sketch[tuple()]         # prints 1
    print sketch[1]               # prints 123
    print sketch["non-existent"]  # prints 0


Install
=======

CountMinSketch is on PyPI, so you can install it with

    pip install countminsketch


License
=======

BSD 3-clause, see the LICENSE file.
