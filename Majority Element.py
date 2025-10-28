class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums.sort()
        
        freq = 0
        n = nums[0]
        l = 0

        for r in range(len(nums)):
            if nums[l] != nums[r]:
                if r - l > freq:
                    freq = r - l
                    n = nums[l]

                l = r

        return nums[-1] if (r - l) + 1 > freq else n
