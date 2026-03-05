from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]   # original copy save
        self.nums = nums[:]       # working copy

    def reset(self) -> List[int]:
        self.nums = self.original[:]   # restore original
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)      # real shuffle
        return self.nums
