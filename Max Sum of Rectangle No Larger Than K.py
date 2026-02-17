import bisect
from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m > n:
            matrix = list(zip(*matrix))
            m, n = n, m
            
        res = float('-inf')
        
        for r1 in range(m):
            col_sums = [0] * n
            for r2 in range(r1, m):
                for c in range(n):
                    col_sums[c] += matrix[r2][c]
                
                max_kadane = float('-inf')
                current_sum = 0
                for x in col_sums:
                    current_sum += x
                    if current_sum > max_kadane:
                        max_kadane = current_sum
                    if current_sum < 0:
                        current_sum = 0
                
                if max_kadane <= k:
                    if max_kadane > res:
                        res = max_kadane
                    if res == k:
                        return k
                    continue
                
                prefix_sums = [0]
                curr_p = 0
                for x in col_sums:
                    curr_p += x
                    idx = bisect.bisect_left(prefix_sums, curr_p - k)
                    if idx < len(prefix_sums):
                        val = curr_p - prefix_sums[idx]
                        if val > res:
                            res = val
                        if res == k:
                            return k
                    bisect.insort(prefix_sums, curr_p)
                    
        return res
