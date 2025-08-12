class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtracking(index,arr):
            if index > len(nums):
                return
            
            for i in range(index, len(nums)):
                if i>index and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                result.append(arr[:])
                backtracking(i+1,arr)
                arr.pop()
        
        result = [[]]
        backtracking(0,[])
        return result
