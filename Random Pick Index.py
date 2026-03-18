import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        """
        Initialize the Solution with an array of integers.
      
        Args:
            nums: List of integers that may contain duplicates
        """
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        Pick a random index where nums[index] == target.
        Uses reservoir sampling to ensure uniform probability distribution.
      
        Args:
            target: The target value to search for in the array
          
        Returns:
            A random index i such that nums[i] == target
        """
        count = 0  # Counter for number of target values found
        result_index = 0  # Store the selected index
      
        # Iterate through the array with index and value
        for index, value in enumerate(self.nums):
            if value == target:
                count += 1
                # Reservoir sampling: with probability 1/count, update the result
                # Generate random number from 1 to count (inclusive)
                random_num = random.randint(1, count)
                # If random number equals count, update the result index
                # This ensures each valid index has equal probability of being selected
                if random_num == count:
                    result_index = index
                  
        return result_index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
