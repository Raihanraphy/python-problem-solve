from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return max(nums)
        memo = [-1] * len(nums)

        def dp(nums, p, memo):
            if p > len(nums)-1:
                return 0
            if memo[p] != -1:
                return memo[p]
            memo[p] = max(dp(nums, p+1, memo), dp(nums, p+2, memo)+ nums[p])
            return memo[p]
        new_home = nums[2:-1]
        print(new_home)
        memo = [-1] * (len(nums) - 3)
        res1 = nums[0] + dp(new_home, 0, memo)
        memo = [-1] * (len(nums)-1)
        res2 = dp(nums[1:], 0, memo)
        
        return max(res1,res2)
        
