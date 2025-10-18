class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largestStart = 0
        localPos, localNeg, largest, largestEnd = 0, 0, nums[0], 0

        for i in range(len(nums)):
            if nums[i] < 0:
                localPos, localNeg = localNeg * nums[i], min(localPos * nums[i], nums[i])
            else:
                localPos, localNeg = max(localPos * nums[i], nums[i]), localNeg * nums[i]

            if localPos > largest and localPos > 0:
                largestEnd = i
                largest = localPos
            elif localNeg > largest:
                largestEnd = i
                largest = localPos
        return largest
