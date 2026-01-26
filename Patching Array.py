from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # The current number helps us reach higher
                miss += nums[i]
                i += 1
            else:
                # We have a gap; patch 'miss' to cover the range up to 2*miss - 1
                miss += miss
                patches += 1
        return patches

# Example Usage:
# sol = Solution()
# print(sol.minPatches(nums = [1,3], n = 6)) # Output: 1
# print(sol.minPatches(nums = [1,5,10], n = 20)) # Output: 2
# print(sol.minPatches(nums = [1,2,2], n = 5)) # Output: 0
