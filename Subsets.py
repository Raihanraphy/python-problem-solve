from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.generate_subsets([], 0, nums, result)
        return result
    
    def generate_subsets(self, subset: List[int], index: int, nums: List[int], result: List[List[int]]):
        # Base case: add the current subset to the result list
        result.append(subset.copy())
        
        # Recursive case
        for i in range(index, len(nums)):
            # Include the current element in the subset
            subset.append(nums[i])
            # Recursively generate subsets starting from the next index
            self.generate_subsets(subset, i + 1, nums, result)
            # Exclude the current element from the subset
            subset.pop()
