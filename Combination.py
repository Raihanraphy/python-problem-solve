from collections import deque
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        # Boundary case
        if n > 20 or k < 1 or k > n:
            return ans
        self.backtrack(ans, n, k, 1, deque())
        return ans

    def backtrack(self, ans: List[List[int]], n: int, k: int, s: int, stack: deque):
        # Base case
        # If k becomes 0
        if k == 0:
            ans.append(list(stack))
            return
        # Start with s till n-k+1
        for i in range(s, n - k + 2):
            stack.append(i)
            # Update start for recursion and decrease k by 1
            self.backtrack(ans, n, k - 1, i + 1, stack)
            stack.pop()

