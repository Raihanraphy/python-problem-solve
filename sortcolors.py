class Solution:
    def sortColors(self, nums):
        zero = 0
        second = len(nums) - 1

        i = 0
        while i <= second:
            while nums[i] == 2 and i < second:
                self.swap(nums, i, second)
                second -= 1
            while nums[i] == 0 and i > zero:
                self.swap(nums, i, zero)
                zero += 1
                i -= 1  # Adjust i after swapping with zero
            i += 1  # Move to the next element

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

