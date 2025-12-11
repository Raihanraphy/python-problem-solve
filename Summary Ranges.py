class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst =[]
        i = 0 
        while i < len(nums):
            start = nums[i]
            while i < len(nums)-1 and nums[i] == nums[i+1] - 1:
                i = i+1 
            if start ==nums[i]:
                lst.append(str(start))
            else:
                lst.append(str(start)+ "->"+ str(nums[i]))
            i = i+1 
        return lst
        
