class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n - 1

        target = nums[0]
        while i <= j:
            mid_i = i + (j - i) // 2
            if nums[mid_i] < target:
                j = mid_i - 1
            else:
                i = mid_i + 1

        return nums[i % n]
