CountMinSketch
==============

This is a minimalistic
`Count-min Sketch <http://en.wikipedia.org/wiki/Count%E2%80%93min_sketch>`
for Python, featuring some cool things like:

 - Being able to count anything that is hash-able by python (numbers, strings,
tuples, inmutables, duck-typeds, etc.).
 - Tests
 - No dependencies
 - No foreign languages, just 100% python.


Usage
=====

.. code-block:: python

    from countminsketch import CountMinSketch
    sketch = CountMinSketch(1000, 10)  # 10 hash functions, 1000 places per hash function
    sketch.update("oh yeah")
    sketch.update(tuple())
    sketch.update(1, value=123)
    print sketch["oh yeah"]       # prints 1
    print sketch[tuple()]         # prints 1
    print sketch[1]               # prints 123
    print sketch["non-existent"]  # prints 0


License
=======

BSD 3-clause, see the LICENSE file.

