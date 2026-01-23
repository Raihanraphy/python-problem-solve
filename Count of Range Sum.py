        
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        sl=SortedList()
        psum=[0]
        for num in nums:
            psum.append(psum[-1]+num)
        n=len(nums)
        res=0
        for i in range(n, -1, -1):
            if i==n:
                sl.add(psum[i])
            else:
                low=lower+psum[i]
                high=upper+psum[i]
                left=sl.bisect_left(low)  # greater or equal
                right=sl.bisect_right(high)-1  # less or equal
                res+=right-left+1
                sl.add(psum[i])
        return res
        
