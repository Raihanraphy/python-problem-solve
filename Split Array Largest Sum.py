class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        mini = max(nums)
        maxi = sum(nums)
        while(mini <= maxi):
            midi = (mini + maxi)//2

            split_array = 1
            temp = 0

            for num in nums:
                temp += num
                if temp > midi:
                    temp = num
                    split_array += 1
            
            if split_array > k:
                mini  = midi + 1
            else:
                maxi = midi -1
        
        return mini

        
