import numpy as np

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        A = np.array(nums, dtype=np.int64)
        
        current_f = np.dot(np.arange(n), A)
        total_sum = np.sum(A)
       
        deltas = total_sum - n * A[::-1]
        f_values = np.zeros(n, dtype=np.int64)
        f_values[0] = current_f
        
        f_values[1:] = current_f + np.cumsum(deltas[:-1])
        
        return int(np.max(f_values))
