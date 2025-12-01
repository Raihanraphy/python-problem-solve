class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x
        mask = xor & -xor
        a = b = 0
        for x in nums:
            if x & mask:
                a ^= x
            else:
                b ^= x
        return [a, b]
