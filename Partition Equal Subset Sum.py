class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = 1

        mask = (1 << (target + 1)) - 1
        for num in nums:
            dp |= (dp << num)  
            dp &= mask         
        return bool((dp >> target) & 1);
