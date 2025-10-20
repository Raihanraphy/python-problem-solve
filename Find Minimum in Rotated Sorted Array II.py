class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]
        left = 0
        right = len(nums)-1
        result = nums[0]
        while left <= right:
            middle = (left + right) // 2
            result = min(result, nums[middle])
            if nums[left] == nums[middle] and nums[middle] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[middle]:
                result = min(result, nums[left])
                left = middle + 1
            else:
                right = middle - 1
        return result
