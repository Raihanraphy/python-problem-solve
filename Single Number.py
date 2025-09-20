class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num  # XOR operation
        return single_number
