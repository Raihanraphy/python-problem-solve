
from typing import List


class WeightedUF:

    def __init__(self):
        self.parent = {}
        self.weight = {}    # weight[x] = x / parent[x]

    def add(self, x: str):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0   # x / x = 1

    def find(self, x: str) -> str:
        """
        Find root with path compression.
        Accumulate weights along the path so that
        weight[x] = x / root after compression.
        """
        if self.parent[x] != x:
            root = self.find(self.parent[x])
            # Before: weight[x] = x / parent[x]
            #         weight[parent[x]] = parent[x] / root  (after recursive compression)
            # After:  weight[x] = x / root = (x / parent[x]) * (parent[x] / root)
            self.weight[x] *= self.weight[self.parent[x]]
            self.parent[x] = root
        return self.parent[x]

    def union(self, a: str, b: str, val: float):
        self.add(a)
        self.add(b)
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.weight[root_a] = val * self.weight[b] / self.weight[a]

    def query(self, a: str, b: str) -> float:
        if a not in self.parent or b not in self.parent:
            return -1.0
        if self.find(a) != self.find(b):
            return -1.0     # not connected
        return self.weight[a] / self.weight[b]


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        uf = WeightedUF()

        for (a, b), val in zip(equations, values):
            uf.union(a, b, val)     # a / b = val

        return [uf.query(a, b) for a, b in queries]
