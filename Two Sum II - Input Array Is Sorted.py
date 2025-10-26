from typing import List
from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      
            
        n = len(numbers)
      
        
        for i in range(n - 1):
           
            complement = target - numbers[i]
          
            
            j = bisect_left(numbers, complement, lo=i + 1)
          
            
            if j < n and numbers[j] == complement:
             
                return [i + 1, j + 1]
