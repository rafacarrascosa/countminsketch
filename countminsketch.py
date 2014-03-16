# -*- coding: utf-8 -*-
import hashlib
import array


class CountMinSketch(object):
    def __init__(self, m, d):
        if not m or not d:
            raise ValueError("Table size (m) and amount of hash functions (d)"
                             " must be non-zero")
        self.m = m
        self.d = d
        self.n = 0
        self.tables = []
        for _ in xrange(d):
            table = array.array("l", (0 for _ in xrange(m)))
            self.tables.append(table)

    def _hash(self, x):
        md5 = hashlib.md5(str(hash(x)))
        for i in xrange(self.d):
            md5.update(str(i))
            yield int(md5.hexdigest(), 16) % self.m

    def update(self, x, value=1):
        self.n += value
        for table, i in zip(self.tables, self._hash(x)):
            table[i] += value

    def query(self, x):
        return min(table[i] for table, i in zip(self.tables, self._hash(x)))

    def __getitem__(self, x):
        return self.query(x)

    def __len__(self):
        return self.n
