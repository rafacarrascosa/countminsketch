# -*- coding: utf-8 -*-
import unittest
from collections import Counter

from countminsketch import CountMinSketch


class TestCountMinSketch(unittest.TestCase):
    def test_zero_at_start(self):
        sketch = CountMinSketch(10, 5)
        for thing in (0, 1, -1, tuple, tuple(), "", "yeah", object()):
            self.assertEqual(sketch.query(thing), 0)

    def test_bad_init(self):
        with self.assertRaises(ValueError):
            CountMinSketch(0, 5)
        with self.assertRaises(ValueError):
            CountMinSketch(100, 0)

    def test_simple_usage(self):
        N = 1000
        sketch = CountMinSketch(10, 5)
        for _ in xrange(N):
            sketch.update("a")
        self.assertEqual(sketch.query("a"), N)
        self.assertEqual(sketch.query("b"), 0)
        self.assertEqual(len(sketch), N)

    def test_syntax_sugar(self):
        sketch = CountMinSketch(10, 5)
        self.assertEqual(sketch.query("a"), sketch["a"])
        sketch.update("a")
        self.assertEqual(sketch.query("a"), sketch["a"])

    def test_counts_overestimate(self):
        text = open(__file__).read()
        counter = Counter(text)
        sketch = CountMinSketch(10, 5)
        for x in text:
            sketch.update(x)
        for x in set(text):
            self.assertGreaterEqual(sketch[x], counter[x])

    def test_updates_greater_than_one(self):
        sketch = CountMinSketch(10, 5)
        sketch.update("a", 123)
        self.assertEqual(sketch.query("a"), 123)


if __name__ == "__main__":
    unittest.main()
